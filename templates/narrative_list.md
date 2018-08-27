# User narratives

{% for obj in yield_objects('NARRATIVE') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}
