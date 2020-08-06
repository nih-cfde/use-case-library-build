# {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->

## Description

{{ obj.content }}

## Requirements

{% if obj.requirements %}

Requirements for this use case:
{% for requirement in obj.requirements %}
* {{ requirement.ident }}: {{ requirement.title }}
{% endfor %}

{% endif %}

## Tasks

{% if obj.user_tasks %}

Tasks for this use case:
{% for task in obj.user_tasks %}
* {{ task.ident }}: {{ task.title }}
{% endfor %}

{% endif %}


{% include "tagblock.html" %}
