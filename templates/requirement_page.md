# {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->
{% if obj.use_cases %}

Use cases that contain this requirement:

{% for uc in obj.use_cases %}
* {{ uc.ident }}: {{ make_title_link(uc) }}
{% endfor %}

{% endif %}


{% if obj.user_tasks %}
## User Tasks

Tasks that contain this requirement:


{% for task in obj.user_tasks %}
* {{ task.ident }}: {{ make_title_link(task) }} - {{ task.blurb }}
{% endfor %}

{% endif %}
