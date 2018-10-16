---
input: Multi-sample VCF
output: QC metrics and filter to apply to variants
task: Variant-level QC of genotype call set
tags:
- !!python/object/new:textblob.blob.Word args: - qc state:   string: qc   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multi-sample vcf state:   string: multi-sample vcf   pos_tag: null
---
