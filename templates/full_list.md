# Introduction

## Use Case Summaries

{% for obj in yield_objects('SUMMARY') %}
* {{ obj.ident }}: {{ make_title_link(obj) }}
{% endfor %}

## User narratives

{% for obj in yield_objects('NARRATIVE') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Personas

{% for obj in yield_objects('PERSONA') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Epics

{% for obj in yield_objects('EPIC') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## User stories

{% for obj in yield_objects('USER STORY') %}
* {{ obj.ident }}: {{ make_title_link(obj) }} - {{ obj.title }}
{% endfor %}
