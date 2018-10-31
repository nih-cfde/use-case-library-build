# {{ obj.title }}

## Persona Description

{{ obj.content }}

## User Narratives and User Epics

{% if obj.narratives %}
User narratives for this persona:
{% for narrative in obj.narratives %}
* {{ narrative.ident }}: {{ make_title_link(narrative) }} - {{ narrative.blurb }}
{% endfor %}{# end for each narrative #}
{% endif %}{# end if obj.narratives #}

(Persona {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% include "tagblock.html" %}
