"""
Library objects.

This contains the code for building/creating the various components of
the Use Case Library.
"""
import os.path

prefixes = {'EPIC': 'EPIC',
            'USERSTORY': 'USER STORY',
            'PERSONA': 'PERSONA',
            'NARRATIVE': 'NARRATIVE',
            'SUMMARY': 'SUMMARY'}

def process_identifier(x):
    "Isolate the ident from the filename."
    if x.endswith('.md'): x = x[:-3]
    return "-".join(x.split('-')[:2])


class Summary(object):
    obj_type = 'SUMMARY'
    template = 'summary_page.md'

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
    template = 'persona_page.md'

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
    template = 'user_story_page.md'

    def __init__(self, ident, inp, output, task, tags):
        self.ident = ident
        self.input = inp
        self.output = output
        self.task = task
        self.title = task
        self.tags = tags
        self.epics = []

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content

    def add_epic(self, epic):
        if epic not in self.epics:
            self.epics.append(epic)


class Narrative(object):
    obj_type = 'NARRATIVE'
    template = 'narrative_page.md'

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
    template = 'epic_page.md'

    def __init__(self, ident, title, blurb, user_stories_str):
        self.ident = ident
        self.title = title
        self.blurb = blurb
        self.user_stories_str = user_stories_str
        self.narrative = None             # parent narrative object

    def resolve_references(self, obj_dict):
        x = []
        for story_str in self.user_stories_str:
            story = obj_dict[process_identifier(story_str)]
            story.add_epic(self)
            x.append(story)

        self.user_stories = x

    def set_narrative(self, obj):
        if self.narrative:
            if self.narrative != obj:
                msg = "for epic {}, narrative already set to {}; cannot set to {}".format(self.ident, self.narrative.ident, obj.ident)
                raise ValueError(msg)
        self.narrative = obj

    def set_content(self, content):
        self.content = content


def get_type(filename):
    basefile = os.path.basename(filename)
    for prefix in prefixes:
        if basefile.startswith(prefix):
            ident = process_identifier(basefile)
            return prefixes[prefix], ident

    raise ValueError("unknown file type: " + basefile)


def create_library_object(filename, header, content):
    """
    Create a library object for the given filename / header combination.
    """
    filetype, ident = get_type(filename)
    if filetype == 'PERSONA':
        if set(header) != set(['title', 'blurb']):
            print('WARNING: extra header components in {}'.format(ident))

        obj = Persona(ident, header['title'], header['blurb'])
    elif filetype == 'USER STORY':
        if 'tags' not in header:
            print('WARNING: no USER STORY tags found in {}'.format(ident))
            header['tags'] = []

        if set(header) != set(['input', 'output', 'task','tags']):
            print('WARNING: extra header components in {}'.format(ident))
            
        obj = UserStory(ident, header['input'], header['output'],
                        header['task'], header['tags'])
    elif filetype == 'NARRATIVE':
        if not set(header).issubset(set(['title', 'blurb', 'persona', 'epics'])):
            print('WARNING: extra header components in {}'.format(ident))
            
        epics = header.get('epics', [])
        if not epics:
            print('WARNING: narrative {} has no epics.'.format(ident))
            epics = []

        obj = Narrative(ident, header['title'], header['blurb'],
                         header['persona'], epics)
    elif filetype == 'EPIC':
        if set(header) != set(['title', 'blurb', 'user-stories']):
            print('WARNING: extra header components in {}'.format(ident))
            
        obj = Epic(ident, header['title'], header['blurb'],
                    header['user-stories'])
    elif filetype == 'SUMMARY':
        if not set(header).issubset(set(['title', 'narratives'])):
            print('WARNING: extra header components in {}'.format(ident))
            
        narratives = header.get('narratives', [])
        if not narratives:
            print('WARNING: summary {} has no narratives.'.format(ident))
            narratives = []

        obj = Summary(ident, header['title'], narratives)
    else:
        raise ValueError('unhandled file type: ' + filetype)

    obj.filename = os.path.basename(filename)
    obj.set_content(content)
    return obj
