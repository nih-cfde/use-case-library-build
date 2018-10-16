---
input: List of gene ontologies and harmonized, multi-study phenotypic data set
output: Phenotypic data files annotated with gene ontologies
task: Use the "annotation propagation rule" to ensure that annotations to ontology terms are "inherited" up
tags:
- !!python/object/new:textblob.blob.Word args: - gene ontologies state:   string: gene ontologies   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - data files state:   string: data files   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-study phenotypic data state:   string: multi-study phenotypic data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
---
