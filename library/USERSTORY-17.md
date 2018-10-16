---
input: Positon-based genomic annotations from multiple sources (e.g. GENCODE, GeneHancer)
output: Aggregation unit definitions (genomic position ranges)
task: Define aggregation units based on genomic positions (e.g. genes, regulatory regions, etc.)
tags:
- !!python/object/new:textblob.blob.Word args: - positon-based state:   string: positon-based   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genomic annotations state:   string: genomic annotations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genomic position state:   string: genomic position   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - gencode state:   string: gencode   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - unit definitions state:   string: unit definitions   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - aggregation state:   string: aggregation   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - multiple sources state:   string: multiple sources   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genehancer state:   string: genehancer   pos_tag: null
---
