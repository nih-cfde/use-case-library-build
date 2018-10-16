---
input: Machine readable activity log and algorithm
output: List of researcher activity that requires manual review
task: "Algorithm compares the data use restrictions to the researcher\u2019s purpose"
tags:
- !!python/object/new:textblob.blob.Word args: - machine state:   string: machine   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - readable activity log state:   string: readable activity log   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - researcher activity state:   string: researcher activity   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - list state:   string: list   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - manual review state:   string: manual review   pos_tag: null
---
