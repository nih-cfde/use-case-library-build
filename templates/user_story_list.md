# User stories

{% for obj in yield_objects('USER STORY') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}
