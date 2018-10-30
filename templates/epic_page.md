# {{ obj.title }}

{% if obj.content %}
## User Epic

{{ obj.content }}
{% endif %}

## User Narrative
{% if obj.narrative %}
Parent narrative: {{ make_title_link(obj.narrative) }} - {{ obj.narrative.blurb }}
{% else %}
(No parent narrative)
{% endif %}

## User Stories
{% if obj.user_stories %}
User stories belonging to this narrative:
{% for story in obj.user_stories %}
* {{ story.ident }}: {{ make_title_link(story) }}
{% endfor %}
{% endif %}

(User Epic {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% include "tagblock.html" %}
