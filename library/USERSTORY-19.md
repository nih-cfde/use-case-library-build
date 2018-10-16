---
input: Variant-based functional annotations (WGSA)
output: Reformatted variant-based functional annotations
task: Parse WGSA output to facilitate queries
tags:
- !!python/object/new:textblob.blob.Word args: - functional annotations state:   string: functional annotations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - variant-based state:   string: variant-based   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - wgsa state:   string: wgsa   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - reformatted state:   string: reformatted   pos_tag: null
---
