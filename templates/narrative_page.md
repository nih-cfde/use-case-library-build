# {{ obj.title }}

{% if obj.summary %}
Summary: {{ make_title_link(obj.summary) }} ({{ obj.ident }})
{% endif %}

## User Narrative

{{ obj.content }}

## User Persona

{% if obj.persona %}
{{ make_title_link(obj.persona) }} - {{ obj.persona.blurb }}
{% endif %}

## User Epics and User Stories

{% if obj.epics %}
User epics under this narrative:

{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
  {% if epic.user_stories %}
    {% for story in epic.user_stories %}
    * {{ story.ident }}: {{ make_title_link(story) }} - Use **{{ story.input }}** to generate **{{ story.output }}**
      by **{{ story.task }}** (story appears in {{ len(story.epics) }} epics total).
    {% endfor %}
  {% endif %}
{% endfor %}

{% endif %}

(User Narrative {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% include "tagblock.html" %}
