---
input: Authenticated log on and COPDGene website
output: Subset of COPDGene clinical, imaging, and genetic data that matches researcher interests
task: Explore clinical variables of interest
tags:
- !!python/object/new:textblob.blob.Word args: - matches researcher interests state:   string: matches researcher interests   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - copdgene state:   string: copdgene   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genetic data state:   string: genetic data   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - subset state:   string: subset   pos_tag: null
---
