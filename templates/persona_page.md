# {{ obj.title }}
(Persona {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

## Blurb

{{ obj.blurb }}

## Full Description:

{{ obj.content }}

{% if obj.narratives %}

User narratives for this persona:
{% for narrative in obj.narratives %}
* {{ narrative.ident }}: {{ make_title_link(narrative) }} - {{ narrative.blurb }}
{% endfor %}

{% endif %}

{% include "tagblock.html" %}
