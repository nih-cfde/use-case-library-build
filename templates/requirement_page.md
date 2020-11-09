# {{ obj.ident }}: {{ obj.title }}

{% if obj.completed %}
## Completion Date: {{obj.completed}}
{% endif %}

## Requirement Description
{{ obj.content }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->
{% if obj.use_cases %}

### Use Cases that contain this Requirement:

{% for uc in obj.use_cases %}
* **{{ uc.ident }}:** {{ make_title_link(uc) }} {{uc.completed}}
{% endfor %}

{% endif %}


{% if obj.user_tasks %}

### User Tasks that contain this Requirement:


{% for task in obj.user_tasks %}
* **{{ task.ident }}:** {{ make_title_link(task) }} {{task.completed}}
{% endfor %}

{% endif %}
