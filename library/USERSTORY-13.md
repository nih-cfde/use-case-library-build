---
input: Multi-sample GDS
output: QC filter to apply to samples
task: Sample-level QC of genotype call set
tags:
- !!python/object/new:textblob.blob.Word args: - qc state:   string: qc   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-sample gds state:   string: multi-sample gds   pos_tag: null
---
