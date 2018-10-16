---
input: Reformatted variant-based functional annotations
output: Variant database
task: Construct database to hold variant-based functional annotations if needed for efficiency of queries
tags:
- !!python/object/new:textblob.blob.Word args: - functional annotations state:   string: functional annotations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - variant state:   string: variant   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - reformatted state:   string: reformatted   pos_tag: null
---
