# {{ obj.title }}
(This is Persona {{ obj.ident }}.)

## Description:

{{ obj.content }}

User narratives for this persona:
{% for narrative in obj.narratives %}
* {{ narrative.ident }}: {{ make_title_link(narrative) }} - {{ narrative.blurb }}
{% endfor %}
