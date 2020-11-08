# {{ obj.ident }}: {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->

{{ obj.content }}

{% if obj.use_cases %}

Use cases that contain this task:

{% for uc in obj.use_cases %}
* {{ uc.ident }}: {{ make_title_link(uc) }}
{% endfor %}

{% endif %}


## Requirements
{% if obj.requirements %}

Requirements belonging to this User Task:

{% for req in obj.requirements %}
* {{ req.ident }}: {{ make_title_link(req) }}
{% endfor %}
{% endif %}
