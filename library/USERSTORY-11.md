---
input: Multi-sample VCF
output: Multi-sample GDS
task: Reformat VCF to GDS (for GENESIS pipeline)
tags:
- !!python/object/new:textblob.blob.Word args: - multi-sample vcf state:   string: multi-sample vcf   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-sample gds state:   string: multi-sample gds   pos_tag: null
---
