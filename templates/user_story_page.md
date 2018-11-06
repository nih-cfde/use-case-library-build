# {{ obj.task }}

Use **{{ make_first_lowercase(obj.input) }}** to **{{ make_first_lowercase(obj.task) }}** to generate **{{ make_first_lowercase(obj.output) }}**.

{% if obj.epics %}
## User Epics

{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}

{% endif %}

{% if obj.content %}
## Description

{{ obj.content }}

{% endif %}

(User Story {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% include "tagblock.html" %}
