---
input: Genetic PCs and KCs
output: Additional sample filter
task: Decide on additional sample exclusions based on PCs and relatedness
tags:
- !!python/object/new:textblob.blob.Word args: - sample filter state:   string: sample filter   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - additional state:   string: additional   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - kcs state:   string: kcs   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genetic pcs state:   string: genetic pcs   pos_tag: null
---
