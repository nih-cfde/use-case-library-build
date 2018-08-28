# {{ obj.task }}
(This is User Story {{ obj.ident }}.)

**Use {{ obj.input }} to generate {{ obj.output }} to {{ obj.task }}**


{% if obj.content %}
## Description:

{{ obj.content }}

{% endif %}
