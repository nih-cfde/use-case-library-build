# {{ obj.title }}
(This is User Narrative {{ obj.ident }}.)

Persona: {{ make_title_link(obj.persona) }}

## Description:

{{ obj.content }}

{% if obj.epics %}

User epics under this narrative:

{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}

  {% if epic.user_stories %}
  {% for story in epic.user_stories %}
> use **{{ story.input }}** to generate **{{ story.output }}** by **{{ story.task }}** (story appears in {{ len(story.epics) }} epics total).
  {% endfor %}
  {% endif %}
{%- endfor %}

{% endif %}
