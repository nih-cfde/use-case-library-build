---
input: CRAM files, interesting variant positions
output: IGV plot (read pileups at variant positon)
task: Evaluate sequence data quality for variants of interest
tags:
- !!python/object/new:textblob.blob.Word args: - variant positon state:   string: variant positon   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - igv state:   string: igv   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - cram state:   string: cram   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - interesting variant positions state:   string: interesting variant positions   pos_tag: null
---
