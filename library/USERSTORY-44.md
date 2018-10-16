---
input: Genotype-Tissue Expression (GTEx) and one phenotypic data set per species, per sex
output: List of expression values for selected genes
task: Search for expression data
tags:
- !!python/object/new:textblob.blob.Word args: - gtex state:   string: gtex   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genotype-tissue expression state:   string: genotype-tissue expression   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - expression values state:   string: expression values   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotypic data state:   string: phenotypic data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
---
