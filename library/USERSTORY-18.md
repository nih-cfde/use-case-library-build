---
input: Variant list; multiple annotation resources
output: Variant-based functional annotations
task: Obtain variant-based genomic annotations
tags:
- !!python/object/new:textblob.blob.Word args: - variant-based state:   string: variant-based   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - functional annotations state:   string: functional annotations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multiple annotation resources state:   string: multiple annotation resources   pos_tag: null
---
