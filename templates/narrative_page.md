# {{ obj.title }}

**ID: {{ obj.ident }}**

<!-- Permalink: ... -->

## Description:

{{ obj.content }}

User epics under this narrative:
{% for epic in obj.epics %}
* {{ epic.ident }}: {{ make_title_link(epic) }} - {{ epic.blurb }}
{% endfor %}
