---
input: Phenotypic data files annotated with gene ontologies and their metadata
output: One phenotypic data set per species, per sex
task: Separate phenotypic data by sex
tags:
- !!python/object/new:textblob.blob.Word args: - phenotypic data state:   string: phenotypic data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - data files state:   string: data files   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - gene ontologies state:   string: gene ontologies   pos_tag: null
---
