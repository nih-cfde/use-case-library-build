---
input: COPDGene cohort and i2b2/tranSMART and variable list
output: Statistical analysis by variable
task: Generate statistical analysis based upon a variable
tags:
- !!python/object/new:textblob.blob.Word args: - variable list state:   string: variable list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - copdgene state:   string: copdgene   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - statistical state:   string: statistical   pos_tag: null
---
