# {{ obj.ident }}: {{ obj.title }}

## Objective Description

{{ obj.content }}

{% if obj.use_cases %}

### Use cases that contain this objective:

{% for uc in obj.use_cases %}
* **{{ uc.ident }}:** {{ make_title_link(uc) }}
{% endfor %}

{% endif %}
