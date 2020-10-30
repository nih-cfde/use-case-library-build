# Contents

## Objectives

{% for obj in yield_objects('OBJECTIVE') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Personas

{% for obj in yield_objects('PERSONA') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Tasks

{% for obj in yield_objects('TASK') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Requirements

{% for obj in yield_objects('REQUIREMENT') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}
