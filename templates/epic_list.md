# Epics

{% for obj in yield_objects('EPIC') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}
