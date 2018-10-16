---
input: Statistical expertise and single dataset with species, sex, expression and phenotype data
output: Table of results for each ontology term with chi-square statistic, p-value, corrected p-value
task: Perform a chi-squared test for each ontology term
tags:
- !!python/object/new:textblob.blob.Word args: - ontology term state:   string: ontology term   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotype data state:   string: phenotype data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - statistical state:   string: statistical   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - chi-square statistic state:   string: chi-square statistic   pos_tag: null
---
