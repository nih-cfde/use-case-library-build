---
input: Cloud workspace with raw datasets and identifiers (SRA, GTEx IDs, etc)
output: Raw datasets matched to identifiers
task: Match datasets to identifiers
tags:
- !!python/object/new:textblob.blob.Word args: - sra state:   string: sra   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - cloud state:   string: cloud   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - raw datasets state:   string: raw datasets   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - gtex ids state:   string: gtex ids   pos_tag: null
---
