# {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->

## Persona

{% if obj.personas %}

{% for persona in obj.personas %}
* {{ persona.ident }}: {{ make_title_link(personas) }}
{% endfor %}

{% endif %}


## Description

{{ obj.content }}

## Requirements

{% if obj.requirements %}

Requirements for this use case:
{% for requirement in obj.requirements %}
* {{ requirement.ident }}: {{ make_title_link(requirement) }}
{% endfor %}

{% endif %}

## Tasks

{% if obj.user_tasks %}

Tasks for this use case:
{% for task in obj.user_tasks %}
* {{ task.ident }}: {{ make_title_link(task) }}
{% endfor %}

{% endif %}


{% include "tagblock.html" %}
