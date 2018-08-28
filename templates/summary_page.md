# {{ obj.title }}
(This is Use Case Summary {{ obj.ident }}.)

<!-- **ID: {{ obj.ident }}** [(permalink)](...) -->

## Description:

{{ obj.content }}

{% if obj.narratives %}

User narratives for this summary:
{% for narrative in obj.narratives %}
* {{ narrative.ident }}: {{ make_title_link(narrative) }} - {{ narrative.blurb }}
{% endfor %}

{% endif %}
