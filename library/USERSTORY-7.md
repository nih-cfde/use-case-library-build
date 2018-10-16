---
input: List of dbGaP variable identifiers for multiple TOPMed studies
output: Selected list of dbGaP variable identifiers for multiple TOPMed studies
task: Select studies and dbGaP variables to use according to which can be sufficiently harmonized
tags:
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - topmed state:   string: topmed   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - variable identifiers state:   string: variable identifiers   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - selected state:   string: selected   pos_tag: null
---
