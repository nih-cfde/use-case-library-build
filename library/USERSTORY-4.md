---
input: Phenotype domain knowledge
output: List of phenotype concepts
task: Define phenotype concepts for primary outcome, covariates and ancillary variables
tags:
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - domain knowledge state:   string: domain knowledge   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotype concepts state:   string: phenotype concepts   pos_tag: null
---
