---
title: Coronary Artery GWAS Summary
narratives:
- NARRATIVE-14
tags:
- !!python/object/new:textblob.blob.Word args: - coronary artery gwas summary state:   string: coronary artery gwas summary   pos_tag: null
---
**Scenarios**

As a statistical geneticist, I would like to
- **enter my research purpose** using a structured ontology and filter down to the list of TOPMed cohorts whose data use restrictions are compatible with my research purpose, so that I know what datasets to apply for access to.
- **apply for access** to TOPMed cohorts using a single application form and have it be reviewed by a centralized IRB.
- **search through TOPMed** (filtered by data use) and identify all individuals that have coronary artery disease. I would like to build a synthetic cohort from this search and push it to a workspace where I can perform analyses on it.
- **launch a variant calling pipeline** across my synthetic cohort to produce a new variant call set, so that it is consistent with other variant call sets that I have utilized previously.
- **upload my own private datasets** to the workspace and form a joint-call set with my synthetic cohort from TOPMed.
- open a Jupyter notebook and **perform a GWAS anaylsis** on these samples, carefully controlling for stratification and other forms of artifact. I would then like to identify genomic loci that are genome-wide significant and pull the variants from these loci into a separate data frame.
- **leverage GTEx and ENCODE datasets** to identify eQTLs within the loci that are genome-wide significant, as well as look at annotations for these loci.