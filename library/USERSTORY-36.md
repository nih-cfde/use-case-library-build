---
input: Genomic coordinates, annotations of interest
output: Genome browser graphic displays
task: Evaluate genomic annotations for variants in region of interest
tags:
- !!python/object/new:textblob.blob.Word args: - genome state:   string: genome   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genomic state:   string: genomic   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - browser graphic displays state:   string: browser graphic displays   pos_tag: null
---
