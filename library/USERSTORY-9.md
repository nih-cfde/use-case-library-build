---
input: dbGaP files with sample, subject and sample-subject mapping IDs
output: Table of study, sample and subject identifiers
task: Select samples (genotype ID) and subjects (phenotype ID) to be used in the analysis
tags:
- !!python/object/new:textblob.blob.Word args: - ids state:   string: ids   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - dbgap files state:   string: dbgap files   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - subject identifiers state:   string: subject identifiers   pos_tag: null
---
