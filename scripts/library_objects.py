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


class LibraryObject(object):
    """
    Base class that defines a method to validate parameters before they are set.
    This keeps the code free of try/except clutter. It validates arbitrary variable names.
    By extending this class, all use case library objects have a validate method
    they can use to validate parameters before setting them.
    """
    def validate(self,param_name,param_value,param_type=None):
        """
        Validate the parameter named param_name is set to 
        non-null value param_value (optionally, enforcing type
        checking to match type param_type).

        param_name :        Name of parameter (string).
                            This will become an attribute of the object

        param_value :       The value to set the parameter to (any type).

        param_type :        (optional) The type of object that param_value
                            should be. If the types of param_value and 
                            param_type do not match, an exception is raised.
        """
        try:
            ident = self.ident
        except AttributeError:
            ident = ""

        if param_value==None:
            # No parameter value was specified,
            err = "Error: parameter %s did not validate, value was None: %s"%(param_name,ident)
            raise Exception(err)

        elif param_type is not None and type(param_type)!=type(param_value):
            # User specified that this paramter
            # should have type X but it had type Y.
            err = "Error: parameter %s had incorrect type, needs type %s but has type %s: %s"%(
                    param_name,
                    type(param_type),
                    type(param_value),
                    ident
            )
            raise Exception(err)

        else:
            setattr(self, param_name, param_value)


class Summary(LibraryObject):
    obj_type = 'SUMMARY'
    template = 'summary_page.md'

    def __init__(self, ident, title, narratives_str, tags):
        self.validate('ident',ident)
        self.validate('title',title)
        self.validate('narratives_str',narratives_str)
        self.validate('tags',tags,[])
        self.tags = [j.lower() for j in self.tags]

    def resolve_references(self, obj_dict):
        x = []
        for narrative_str in self.narratives_str:
            try:
                narrative_obj = obj_dict[process_identifier(narrative_str)]
            except KeyError:
                raise Exception("ERROR: Could not find narrative %s"%(narrative_str))
            narrative_obj.set_summary(self)
            x.append(narrative_obj)
        self.narratives = x

    def set_content(self, content):
        self.content = content


class Persona(LibraryObject):
    obj_type = 'PERSONA'
    template = 'persona_page.md'

    def __init__(self, ident, title, blurb, tags):
        self.validate('ident',ident)
        self.validate('title',title)
        self.validate('blurb',blurb)
        self.validate('tags',tags,[])
        self.tags = [j.lower() for j in self.tags]
        self.narratives = []

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content

    def add_narrative(self, obj):
        assert obj.obj_type == 'NARRATIVE'
        self.narratives.append(obj)
        # Note: narratives will not be sorted
        # when we retrieve this later


class UserStory(LibraryObject):
    obj_type = 'USER STORY'
    template = 'user_story_page.md'

    def __init__(self, ident, inp, output, task, tags):
        self.validate('ident',ident)
        self.validate('title',task)
        self.validate('task',task)
        self.validate('input',inp)
        self.validate('output',output)
        self.validate('tags',tags,[])
        self.tags = [j.lower() for j in self.tags]
        self.epics = []

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content

    def add_epic(self, epic):
        if epic not in self.epics:
            self.epics.append(epic)


class Narrative(LibraryObject):
    obj_type = 'NARRATIVE'
    template = 'narrative_page.md'

    def __init__(self, ident, title, blurb, persona_str, epics_str, tags):
        self.validate('ident',ident,"")
        self.validate('title',title,"")
        self.validate('blurb',blurb,"")
        self.validate('persona_str',persona_str,"")
        self.validate('epics_str',epics_str,[]) # epics that belong to this narrative
        self.validate('tags',tags,[])
        self.tags = [j.lower() for j in self.tags]
        self.summary = None
        self.persona = None
        self.epics = []

    def resolve_references(self, obj_dict):
        x = []
        for epic in self.epics_str:
            epic_key = process_identifier(epic)
            if epic_key not in obj_dict.keys():
                err = "Error: Missing epic %s, listed in narrative %s: "%(epic_key,self.ident)
                err += "no epic file for %s exists in library/ directory"%(epic_key)
                raise Exception(err)
            epic_obj = obj_dict[epic_key]
            epic_obj.set_narrative(self)
            x.append(epic_obj)
        self.epics = x

        try:
            self.persona = obj_dict[process_identifier(self.persona_str)]
        except AssertionError:
            err = "Error: persona process identifier was not a single item. "
            err += "Try proving a single item instead of a list. "
            err += "File: %s"%(self.ident)
            raise Exception(err)

        self.persona.add_narrative(self)

    def set_content(self, content):
        self.content = content

    def set_summary(self, obj):
        if self.summary:
            assert self.summary == obj, obj.ident
        self.summary = obj


class Epic(LibraryObject):
    obj_type = 'EPIC'
    template = 'epic_page.md'

    def __init__(self, ident, title, blurb, user_stories_str, tags):
        self.validate('ident',ident)
        self.validate('title',title)
        self.validate('blurb',blurb)
        self.validate('user_stories_str',user_stories_str)
        self.validate('tags',tags,[])
        self.narrative = None             # parent narrative object
        self.user_stories = []

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
        if 'tags' not in header:
            header['tags'] = []

        required = ['title', 'blurb','tags']
        if set(header) != set(required):
            print('WARNING: extra header components in {}'.format(ident))
            print('header   = %s'%(", ".join(header.keys())))
            print('required = %s'%(", ".join(required)))

        obj = Persona(ident, header['title'], header['blurb'], header['tags'])

    elif filetype == 'USER STORY':
        if 'tags' not in header:
            header['tags'] = []

        required = ['input','output','task','tags']
        if set(header) != set(required):
            print('WARNING: extra header components in {}'.format(ident))
            print('header   = %s'%(", ".join(header.keys())))
            print('required = %s'%(", ".join(required)))
            
        obj = UserStory(ident, header['input'], header['output'], header['task'], header['tags'])

    elif filetype == 'NARRATIVE':
        if 'tags' not in header:
            header['tags'] = []

        required = ['title','blurb', 'persona', 'epics','tags']
        if set(header) != set(required):
            print('WARNING: extra header components in {}'.format(ident))
            print('header   = %s'%(", ".join(header.keys())))
            print('required = %s'%(", ".join(required)))
            
        epics = header.get('epics', [])
        if not epics:
            print('WARNING: narrative {} has no epics.'.format(ident))
            epics = []

        obj = Narrative(ident, header['title'], header['blurb'], header['persona'], epics, header['tags'])

    elif filetype == 'EPIC':
        if 'tags' not in header:
            header['tags'] = []

        required = ['title', 'blurb', 'user-stories','tags']
        if set(header) != set(required):
            print('WARNING: extra header components in {}'.format(ident))
            print('header   = %s'%(", ".join(header.keys())))
            print('required = %s'%(", ".join(required)))
            
        obj = Epic(ident, header['title'], header['blurb'],
                    header['user-stories'], header['tags'])

    elif filetype == 'SUMMARY':
        if 'tags' not in header:
            header['tags'] = []

        required = ['title','narratives','tags']
        if set(header) != set(required):
            print('WARNING: extra header components in {}'.format(ident))
            print('header   = %s'%(", ".join(header.keys())))
            print('required = %s'%(", ".join(required)))
            
        narratives = header.get('narratives', [])
        if not narratives:
            print('WARNING: summary {} has no narratives.'.format(ident))
            narratives = []

        obj = Summary(ident, header['title'], narratives, header['tags'])

    else:
        raise ValueError('unhandled file type: ' + filetype)

    obj.filename = os.path.basename(filename)
    obj.set_content(content)
    return obj

