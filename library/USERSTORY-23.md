---
input: Statisical analysis plan & list of available analysis pipelines
output: Analysis pipeline choice
task: Select analysis pipeline (GENESIS illustrated here)
tags:
- !!python/object/new:textblob.blob.Word args: - analysis plan state:   string: analysis plan   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - available analysis pipelines state:   string: available analysis pipelines   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - pipeline choice state:   string: pipeline choice   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - statisical state:   string: statisical   pos_tag: null
---
