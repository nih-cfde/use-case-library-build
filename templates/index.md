# Use Case Library

This Library contains a collection of Use Cases for the
[NIH Data Commons Pilot Phase Consortium](https://nihdatacommons.us/).
Note, not all use cases are being prioritized for implementation!

For the structure of the Use Case Library, please see
[the use case glossary](./glossary/).

If you want to contribute a new user narrative, please
[make a copy of this template document](use-case-template.md),
modify it, and then
[create a new issue on GitHub under dcppc/use-case-library/](https://github.com/dcppc/use-case-library/issues). Alternatively,
you can submit it to dcppc.inbox@gmail.com, or follow the detailed instructions in the [Contributing Guidelines](CONTRIBUTING.md).

## Use Case Summaries

{% for obj in yield_objects('SUMMARY') %}
* {{ make_title_link(obj) }}
{% endfor %}

## Full Listing of Library Entries

View the comprehensive list of library entries [here](full_list.md).

The Use Case Library contains {{ len(yield_objects('SUMMARY')) }} use
case summaries, {{ len(yield_objects('NARRATIVE')) }} user narratives,
{{ len(yield_objects('EPIC')) }} user epics, and 
{{ len(yield_objects('USER STORY')) }} user stories, for 
{{ len(yield_objects('PERSONA')) }} personas.
