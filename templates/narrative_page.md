# {{ obj.title }}
(User Narrative {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

Persona: {{ make_title_link(obj.persona) }}

## Blurb

{{ obj.blurb }}

## Full Description:

{{ obj.content }}

## Related Library Items

{% if obj.epics %}

User epics under this narrative:

{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
  {% if epic.user_stories %}
    {% for story in epic.user_stories %}
    * **User Story:** use **{{ story.input }}** to generate **{{ story.output }}**
      by **{{ story.task }}** (story appears in {{ len(story.epics) }} epics total).
    {% endfor %}
  {% endif %}
{% endfor %}

{% endif %}

{% include "tagblock.html" %}
