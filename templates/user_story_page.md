# {{ obj.task }}
(This is User Story {{ obj.ident }}.)

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
