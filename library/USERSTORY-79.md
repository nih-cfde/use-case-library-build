---
input: Imaging features of interest and table of anatomical aberrations associated with the genetic and phenotypic variations
output: A notebook configuration JSON file which will be used by the BioJupies API to generate the notebook containing an analysis of the GTEx samples
task: Generate subject lists and variables for subsequent analyses
tags:
- !!python/object/new:textblob.blob.Word args: - gtex state:   string: gtex   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - imaging state:   string: imaging   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - phenotypic variations state:   string: phenotypic variations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - biojupies api state:   string: biojupies api   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - notebook configuration state:   string: notebook configuration   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - anatomical aberrations state:   string: anatomical aberrations   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - json state:   string: json   pos_tag: null
---
