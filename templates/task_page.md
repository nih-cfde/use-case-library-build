# {{ obj.ident }}: {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->
## User Task Description

{{ obj.content }}

{% if obj.use_cases %}

### Use cases that contain this User Task:

{% for uc in obj.use_cases %}
* **{{ uc.ident }}:** {{ make_title_link(uc) }}
{% endfor %}
{% endif %}



{% if obj.requirements %}

### Requirements belonging to this User Task:

{% for req in obj.requirements %}
* **{{ req.ident }}:** {{ make_title_link(req) }}
{% endfor %}
{% endif %}
