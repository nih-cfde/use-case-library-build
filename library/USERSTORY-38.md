---
input: Tissues of interest; variant identifiers and positions
output: Expression data on variants and tissues of interest
task: Evaluate genomic annotations for variants in region of interest
tags:
- !!python/object/new:textblob.blob.Word args: - expression state:   string: expression   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - variant identifiers state:   string: variant identifiers   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - tissues state:   string: tissues   pos_tag: null
---
