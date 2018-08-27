# Personas

{% for obj in yield_objects('PERSONA') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}
