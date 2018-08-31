# {{ obj.title }}
(User Epic {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% if obj.narrative %}
Parent narrative: {{ make_title_link(obj.narrative) }} - {{ obj.narrative.blurb }}
{% else %}
(no parent narrative)
{% endif %}

{% if obj.user_stories %}

User stories belonging to this narrative:
{% for story in obj.user_stories %}
* {{ story.ident }}: {{ make_title_link(story) }}
{% endfor %}

{% endif %}

{% if obj.content %}

## Description:

{{ obj.content }}

{% endif %}
