# {{ obj.title }}
(This is User Epic {{ obj.ident }}.)

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
