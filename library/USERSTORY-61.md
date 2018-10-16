---
input: List of applicable datasets and appropriate credentials
output: Cloud workspace with raw datasets
task: Load data to workspace
tags:
- !!python/object/new:textblob.blob.Word args: - cloud state:   string: cloud   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - raw datasets state:   string: raw datasets   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - applicable datasets state:   string: applicable datasets   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - appropriate credentials state:   string: appropriate credentials   pos_tag: null
---
