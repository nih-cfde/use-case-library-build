---
input: Analysis pipeline software modules (in docker image)
output: CWL analysis pipeline
task: Create and install CWL analysis pipeline
tags:
- !!python/object/new:textblob.blob.Word args: - docker image state:   string: docker image   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - analysis pipeline state:   string: analysis pipeline   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - cwl state:   string: cwl   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - pipeline software modules state:   string: pipeline software modules   pos_tag: null
---
