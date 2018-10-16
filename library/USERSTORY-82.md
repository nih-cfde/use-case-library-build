---
input: A list of computational tools and selected tool parameters
output: A notebook configuration JSON file which will be used by the BioJupies API to generate the notebook containing an analysis of the GTEx samples
task: Use the computational tool selection interface on BioJupies to select and customize the downstream analysis
tags:
- !!python/object/new:textblob.blob.Word args: - computational tools state:   string: computational tools   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - gtex state:   string: gtex   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - biojupies api state:   string: biojupies api   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - notebook configuration state:   string: notebook configuration   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - tool parameters state:   string: tool parameters   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - json state:   string: json   pos_tag: null
---
