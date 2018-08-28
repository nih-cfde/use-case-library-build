# {{ obj.title }}
(This is User Narrative {{ obj.ident }}.)

Persona: {{ make_title_link(obj.persona) }}

## Description:

{{ obj.content }}

{% if obj.epics %}

User epics under this narrative:
{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}

{% endif %}
