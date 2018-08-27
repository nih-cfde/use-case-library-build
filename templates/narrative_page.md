# {{ obj.title }}

**ID: {{ obj.ident }}** [(permalink)](...)

Persona: {{ make_title_link(obj.persona) }}

## Description:

{{ obj.content }}

User epics under this narrative:
{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}
