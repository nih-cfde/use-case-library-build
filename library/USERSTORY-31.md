---
input: Inputs to CWL analysis pipeline, previously associated variant IDs
output: Model fit statistics, association test statistics, interesting variant positions
task: Check for novel hits by running association analysis, while conditioning on previously associated variants
tags:
- !!python/object/new:textblob.blob.Word args: - analysis pipeline state:   string: analysis pipeline   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - cwl state:   string: cwl   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - inputs state:   string: inputs   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - model state:   string: model   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - ids state:   string: ids   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - association test statistics state:   string: association test statistics   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - fit statistics state:   string: fit statistics   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - interesting variant positions state:   string: interesting variant positions   pos_tag: null
---
