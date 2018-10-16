---
input: Expression data separated by sex and phenotypic data files annotated with gene ontologies
output: Single dataset with species, sex, expression and phenotype data
task: Finalize dataset
tags:
- !!python/object/new:textblob.blob.Word args: - gene ontologies state:   string: gene ontologies   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotype data state:   string: phenotype data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - expression state:   string: expression   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotypic data files state:   string: phenotypic data files   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - single state:   string: single   pos_tag: null
---
