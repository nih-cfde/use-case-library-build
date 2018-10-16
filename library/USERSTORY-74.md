---
input: COPDGene cohort and i2b2/tranSMART
output: Table with subject totals and statistical analysis by age, sex and race for each subset, if data are available
task: Generate summary statistics
tags:
- !!python/object/new:textblob.blob.Word args: - copdgene state:   string: copdgene   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - statistical analysis state:   string: statistical analysis   pos_tag: null
---
