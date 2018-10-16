---
input: Single-sample VCFs
output: Multi-sample VCF
task: Prepare genotypic data - assemble single-sample VCFs
tags:
- !!python/object/new:textblob.blob.Word args: - single-sample vcfs state:   string: single-sample vcfs   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-sample vcf state:   string: multi-sample vcf   pos_tag: null
---
