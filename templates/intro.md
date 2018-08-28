# Use Case Library

{% for obj in yield_objects('SUMMARY') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## [Full listing of library entries](full_list.md)

The Use Case Library contains {{ len(yield_objects('SUMMARY')) }} use
case summaries, {{ len(yield_objects('NARRATIVE')) }} user narratives,
{{ len(yield_objects('EPIC')) }} user epics, and 
{{ len(yield_objects('USER STORY')) }} user stories, for 
{{ len(yield_objects('PERSONA')) }} personas.
