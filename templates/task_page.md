# {{ obj.ident }}: {{ obj.title }}

{% if obj.completed %}
## Completion Date: {{obj.completed}}
{% endif %}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->
## User Task Description

{{ obj.content }}

{% if obj.use_cases %}

### Use cases that contain this User Task:

{% for uc in obj.use_cases %}
* **{{ uc.ident }}:** {{ make_title_link(uc) }} {{uc.completed}}
{% endfor %}
{% endif %}



{% if obj.requirements %}

### Requirements belonging to this User Task:

{% for req in obj.requirements %}
* **{{ req.ident }}:** {{ make_title_link(req) }} {{req.completed}}
{% endfor %}
{% endif %}
