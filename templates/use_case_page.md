# {{ obj.title }}

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->

## Description

{{ obj.content }}

## User Narratives

{% if obj.narratives %}

User narratives for this summary:
{% for narrative in obj.narratives %}
* {{ narrative.ident }}: {{ make_title_link(narrative) }} - {{ narrative.blurb }}
{% endfor %}

{% endif %}

(Use Case Summary {{ obj.ident }} - {{ make_view_link(obj, "view source") }} | {{ make_edit_link(obj, "edit") }})

{% include "tagblock.html" %}
