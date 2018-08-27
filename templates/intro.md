# Introduction

## User narratives

{% for obj in yield_objects('NARRATIVE') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Personas

{% for obj in yield_objects('PERSONA') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## Epics

{% for obj in yield_objects('EPIC') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}

## User stories

{% for obj in yield_objects('USER STORY') %}
* {{ make_title_link(obj) }} - {{ obj.blurb }}
{% endfor %}
