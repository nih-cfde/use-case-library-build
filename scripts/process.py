#! /usr/bin/env python
import sys
import argparse
import yaml
import os
import shutil

from jinja2 import Environment, FileSystemLoader

prefixes = {'EPIC': 'EPIC',
            'USERSTORY': 'USER STORY',
            'PERSONA': 'PERSONA',
            'NARRATIVE': 'NARRATIVE',
            'SUMMARY': 'SUMMARY'}

templates = {'EPIC': 'epic_page.md',
             'USER STORY': 'user_story_page.md',
             'PERSONA': 'persona_page.md',
             'NARRATIVE': 'narrative_page.md',
             'SUMMARY': 'summary_page.md'}

def process_identifier(x):
    return "-".join(x.split('-')[:2])


class Summary(object):
    obj_type = 'SUMMARY'

    def __init__(self, ident, title, narratives_str):
        self.ident = ident
        self.title = title
        self.narratives_str = narratives_str

    def resolve_references(self, obj_dict):
        x = []
        for narrative_str in self.narratives_str:
            narrative_obj = obj_dict[process_identifier(narrative_str)]
            narrative_obj.set_summary(self)
            x.append(narrative_obj)
        self.narratives = x

    def set_content(self, content):
        self.content = content


class Persona(object):
    obj_type = 'PERSONA'

    def __init__(self, ident, title, blurb):
        self.ident = ident
        self.title = title
        self.blurb = blurb
        self.narratives = []

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content

    def add_narrative(self, obj):
        assert obj.obj_type == 'NARRATIVE'
        self.narratives.append(obj)


class UserStory(object):
    obj_type = 'USER STORY'

    def __init__(self, ident, title, blurb):
        self.ident = ident
        self.title = title
        self.blurb = blurb

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content


class Narrative(object):
    obj_type = 'NARRATIVE'

    def __init__(self, ident, title, blurb, persona_str, epics_str):
        self.ident = ident
        self.title = title
        self.blurb = blurb
        self.persona_str = persona_str
        self.epics_str = epics_str        # epics that belong to this narrative
        self.summary = None

    def resolve_references(self, obj_dict):
        x = []
        for epic in self.epics_str:
            epic_obj = obj_dict[process_identifier(epic)]
            epic_obj.set_narrative(self)
            x.append(epic_obj)
        self.epics = x

        persona = obj_dict[process_identifier(self.persona_str)]
        self.persona = persona
        persona.add_narrative(self)

    def set_content(self, content):
        self.content = content

    def set_summary(self, obj):
        if self.summary:
            assert self.summary == obj, obj.ident
        self.summary = obj


class Epic(object):
    obj_type = 'EPIC'

    def __init__(self, ident, title, blurb, user_stories_str):
        self.ident = ident
        self.title = title
        self.blurb = blurb
        self.user_stories_str = user_stories_str
        self.narrative = None             # parent narrative object

    def resolve_references(self, obj_dict):
        x = []
        for story in self.user_stories_str:
            x.append(obj_dict[process_identifier(story)])
        self.user_stories = x

    def set_narrative(self, obj):
        if self.narrative:
            assert self.narrative == obj, obj.ident
        self.narrative = obj

    def set_content(self, content):
        self.content = content


def get_type(filename):
    for prefix in prefixes:
        if filename.startswith(prefix):
            ident = process_identifier(filename)
            return prefixes[prefix], ident

    raise ValueError("unknown file type: " + filename)


def validate_header(filename, header):
    filetype, ident = get_type(filename)
    if filetype == 'PERSONA':
        return Persona(ident, header['title'], header['blurb'])
    elif filetype == 'USER STORY':
        return UserStory(ident, header['title'], header['blurb'])
    elif filetype == 'NARRATIVE':
        epics = header.get('epics', [])
        if not epics:
            print('WARNING: narrative {} has no epics.'.format(ident))
            epics = []

        return Narrative(ident, header['title'], header['blurb'],
                         header['persona'], epics)
    elif filetype == 'EPIC':
        return Epic(ident, header['title'], header['blurb'],
                    header['user-stories'])
    elif filetype == 'SUMMARY':
        narratives = header.get('narratives', [])
        if not narratives:
            print('WARNING: summary {} has no narratives.'.format(ident))
            narratives = []

        return Summary(ident, header['title'], narratives)
    else:
        raise ValueError('unhandled file type: ' + filetype)


def main(argv=sys.argv[1:]):
    p = argparse.ArgumentParser()
    p.add_argument('inputfiles', nargs='+')
    args = p.parse_args(argv)

    jinja_env = Environment(
        loader=FileSystemLoader('../templates')
    )

    obj_dict = {}
    for filename in args.inputfiles:
        lines = open(filename, 'rt').readlines()
        lines = [ x.rstrip() for x in lines ]
        assert lines[0].startswith('---')

        header_end = None
        for i, x in enumerate(lines[1:]):
            if x.startswith('---'):
                header_end = i+1
                break

        assert header_end, "no header found"

        # grab the yaml & the rest
        header = lines[0:i+1]
        rest = lines[i+2:]

        yyheader = yaml.load("\n".join(header))

        obj = validate_header(filename, yyheader)
        if obj.ident in obj_dict:
            raise Exception("duplicate identity: " + obj.ident)

        obj_dict[obj.ident] = obj
        obj.set_content("\n".join(rest))

    print('loaded {} objects'.format(len(obj_dict)))

    print('resolving references')
    for obj in obj_dict.values():
        obj.resolve_references(obj_dict)

    def yield_objects(obj_type):
        x = []
        for obj in obj_dict.values():
            if obj.obj_type == obj_type:
                x.append((obj.ident, obj))

        return [ obj for _, obj in sorted(x) ]

    try:
        shutil.rmtree('../output/docs')
    except FileNotFoundError:
        pass

    try:
        os.mkdir('../output')
    except FileExistsError:
        pass
    os.mkdir('../output/docs')

    def make_title_link(obj):
        return "[{}]({})".format(obj.title, obj.ident + '.md')

    def render_template(filename, outpath=None, **kw):
        if not outpath:
            outpath = os.path.join('../output/docs', filename)

        template = jinja_env.get_template(filename)
        with open(outpath, 'wt') as fp:
            print('creating:', outpath)
            print(template.render(yield_objects=yield_objects, make_title_link=make_title_link, len=len, **kw), file=fp)

    render_template('intro.md')
    render_template('full_list.md')
    render_template('mkdocs.yml', '../output/mkdocs.yml')

    for obj in obj_dict.values():
        filename = os.path.join('../output/docs', obj.ident + '.md')
        template_name = templates[obj.obj_type]
        render_template(template_name, filename, obj=obj)


if __name__ == '__main__':
    main()
