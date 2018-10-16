---
input: All GTEx tissue samples and selected metadata elements such as tissue type and age
output: Two cohorts of GTEx tissue samples which will be used to generate a signature
task: Use the dedicated application that is part of BioJupies to create a collection of signatures for young vs old tissues across all GTEx tissues
tags:
- !!python/object/new:textblob.blob.Word args: - gtex state:   string: gtex   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - tissue type state:   string: tissue type   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - metadata elements state:   string: metadata elements   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - tissue samples state:   string: tissue samples   pos_tag: null
---
