# Contents

## Use Cases

{% for uc in yield_objects('USE CASE') %}
* {{ uc.ident }}: {{ make_title_link(uc) }}
{% endfor %}

## Objectives

{% for obj in yield_objects('OBJECTIVE') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}

## Personas

{% for obj in yield_objects('PERSONA') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}

## Tasks

{% for obj in yield_objects('TASK') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}

## Requirements

{% for obj in yield_objects('REQUIREMENT') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}
