---
input: Multi-sample GDS & filters
output: GRM
task: Estimate Genetic Relatedness Matrix (GRM)
tags:
- !!python/object/new:textblob.blob.Word args: - grm state:   string: grm   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-sample gds state:   string: multi-sample gds   pos_tag: null
---
