# {{ obj.title }}
(User Narrative {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

Persona: {{ make_title_link(obj.persona) }}

## Description:

{{ obj.content }}

{% if obj.epics %}

User epics under this narrative:
{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}

{% endif %}
