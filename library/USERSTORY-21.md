---
input: User-specified filtering criteria and variant database
output: Variant filters
task: Define variant filters for input to analysis software
tags:
- !!python/object/new:textblob.blob.Word args: - variant database state:   string: variant database   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - user-specified state:   string: user-specified   pos_tag: null
---
