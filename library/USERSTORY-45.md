---
input: Expression data files and their metadata
output: Expression data separated by sex
task: Annotate expression data by sex
tags:
- !!python/object/new:textblob.blob.Word args: - expression state:   string: expression   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - data files state:   string: data files   pos_tag: null
---
