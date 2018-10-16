---
title: Perform more detailed analyses
blurb: Coronary artery disease (CAD) genome-wide association user narrative.
user-stories:
- USERSTORY-2
tags:
- !!python/object/new:textblob.blob.Word args: - coronary state:   string: coronary   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - cad state:   string: cad   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - perform state:   string: perform   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - genome-wide association user narrative state:   string: genome-wide association user narrative   pos_tag: null
- !!python/object/new:textblob.blob.Word args: - artery disease state:   string: artery disease   pos_tag: null
---
Identify a credible set of causal variants at each genome-wide significant locus.
For each variant in each of the credible sets, utilize the GTEx dataset to perform an eQTL analysis that associates each variant within each of the credible sets with the expression of nearby genes.
Leverage ENCODE datasets to look at potential annotations associated with non-coding variants in the credible sets.