# {{ obj.ident }}: {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->
{% if obj.completed %}
## Completion Date: {{obj.completed}}
{% endif %}

{% if obj.tutorial %}
### {{obj.tutorial}}
{% endif %}

{% if obj.tutorial %}
## NIH Goal:

{{obj.goal}}
{% endif %}

## Persona

{% if obj.personas %}

{% for persona in obj.personas %}
**{{ persona.ident }}:** {{ make_title_link(persona) }}
{% endfor %}

{% else %}

no personas.

{% endif %}

## Objective


{% if obj.objectives %}

{% for objective in obj.objectives %}
**{{ objective.ident }}:** {{ make_title_link(objective) }}
{% endfor %}

{% else %}

no objectives.

{% endif %}

## Description

{{ obj.content }}



{% if obj.user_tasks %}
## Tasks for this use case:

{% for task in obj.user_tasks %}
* **{{ task.ident }}:** {{ make_title_link(task) }} {{task.completed}}
{% endfor %}

{% endif %}




{% if obj.requirements %}

## Requirements for this use case:
{% for requirement in obj.requirements %}
* **{{ requirement.ident }}:** {{ make_title_link(requirement) }} {{requirement.completed}}
{% endfor %}

{% endif %}


{% include "tagblock.html" %}
