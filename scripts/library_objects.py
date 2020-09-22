"""
Library objects.

This contains the code for building/creating the various components of
the Use Case Library.
"""
import os.path

prefixes = {'uc': 'USE CASE',
            't': 'TASK',
            'r': 'REQUIREMENT',
            'USERSTORY': 'USER STORY',
            'p': 'PERSONA',
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
            err = "Error: library item %s: parameter %s did not validate, value was None"%(ident,param_name)
            raise Exception(err)

        elif param_type is not None and type(param_type)!=type(param_value):
            # User specified that this paramter
            # should have type X but it had type Y.
            err = "Error: library item %s: parameter %s had incorrect type, needs type %s but has type %s: %s"%(
                    ident,
                    param_name,
                    type(param_type),
                    type(param_value)
            )
            raise Exception(err)

        else:
            setattr(self, param_name, param_value)


class UseCase(LibraryObject):
    obj_type = 'USE CASE'
    template = 'use_case_page.md'

    def __init__(self, ident, title, persona, objective, user_tasks, requirements):
        self.ident = ident
        self.validate('title', title)
        self.validate('persona', persona)
        self.validate('objective', objective)
        self.validate('user_task_names', user_tasks, [])
        self.validate('requirement_names', requirements, [])
        self.user_tasks = []
        self.requirements = []

    def resolve_references(self, obj_dict):

        for task_name in self.user_task_names:
            try:
                task = obj_dict[task_name]
                self.user_tasks.append(task)
                task.add_use_case(self)
            except KeyError:
                raise Exception(f"could not find task {task_name} for use case {self.ident}")

        for requirement_name in self.requirement_names:
            try:
                req = obj_dict[requirement_name]
                self.requirements.append(req)
                req.add_use_case(self)
            except KeyError:
                raise Exception(f"could not find requirement {requirement_name} for use case {self.ident}")

    def set_content(self, content):
        self.content = content


class Task(LibraryObject):
    obj_type = 'TASK'
    template = 'task_page.md'

    def __init__(self, ident, title):
        self.ident = ident
        self.validate('title', title)
        self.use_cases = []

    def resolve_references(self, obj_dict):
        pass

    def set_content(self, content):
        self.content = content

    def add_use_case(self, uc):
        if uc not in self.use_cases:
            self.use_cases.append(uc)


class Requirement(LibraryObject):
    obj_type = 'REQUIREMENT'
    template = 'requirement_page.md'

    def __init__(self, ident, title):
        self.ident = ident
        self.validate('title', title)
        self.use_cases = []

    def resolve_references(self, obj_dict):
        pass

    def set_content(self, content):
        self.content = content

    def add_use_case(self, uc):
        if uc not in self.use_cases:
            self.use_cases.append(uc)


class Persona(LibraryObject):
    obj_type = 'PERSONA'
    template = 'persona_page.md'

    def __init__(self, ident, title):
        self.ident = ident
        self.validate('title', title)
        self.use_cases = []
        #self.validate('blurb',blurb)
        #self.validate('tags',tags,[])
        #self.tags = [j.lower() for j in self.tags]
        #self.narratives = []

    def resolve_references(self, obj_dict): pass

    def set_content(self, content):
        self.content = content

    def add_use_case(self, uc):
        if uc not in self.use_cases:
            self.use_cases.append(uc)
        # Note: narratives will not be sorted
        # when we retrieve this later


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
    if filetype == 'USE CASE':
        obj = UseCase(ident, header['title'], header['persona'],
                      header['objective'], header['user_tasks'],
                      header['requirements'])
    elif filetype == 'TASK':
        obj = Task(ident, header['title'])
    elif filetype == 'REQUIREMENT':
        obj = Requirement(ident, header['title'])
    elif filetype == 'PERSONA':
        obj = Persona(ident, header['title'])
    else:
        raise ValueError('unhandled file type: ' + filetype)

    obj.filename = os.path.basename(filename)
    obj.set_content(content)
    return obj
