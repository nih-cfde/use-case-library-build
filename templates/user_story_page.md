# {{ obj.task }}
(User Story {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

**Use {{ obj.input }} to generate {{ obj.output }} to {{ obj.task }}**

{% if obj.epics %}

{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}

{% endif %}


{% if obj.content %}
## Description:

{{ obj.content }}

{% endif %}

{% include "tagblock.html" %}
