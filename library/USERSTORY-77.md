---
input: COPDGene cohort and Chest Imaging Platform
output: Images ready for analysis
task: Render the images and visualize the anatomical structures
tags:
- !!python/object/new:textblob.blob.Word args: - images state:   string: images   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - copdgene state:   string: copdgene   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - chest imaging platform state:   string: chest imaging platform   pos_tag: null
---
