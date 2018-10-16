---
input: List of phenotype concepts and dbGaP data files
output: List of dbGaP variable identifiers for multiple TOPMed studies
task: Search metadata to identify dbGaP variables corresponding to phenotype concepts
tags:
- !!python/object/new:textblob.blob.Word args: - variable identifiers state:   string: variable identifiers   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotype concepts state:   string: phenotype concepts   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - topmed state:   string: topmed   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - dbgap data files state:   string: dbgap data files   pos_tag: null
---
