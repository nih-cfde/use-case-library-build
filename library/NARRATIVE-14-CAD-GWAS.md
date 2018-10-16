---
title: Coronary Artery GWAS User Narrative
persona: PERSONA-7-statistical-geneticist
blurb: Identify genetic risk factors for coronary artery disease.
epics:
- EPIC-18
- EPIC-19
- EPIC-20
- EPIC-21
tags:
- identify
- genetic risk factors
- coronary artery disease
- coronary artery gwas user narrative
---
### Scientific Objective

Genome-wide association studies (GWAS), where variants across the genome are tested for association with a phenotype of interest, are widely used in human genetics research. The primary output of these studies is the identification of genetic loci that have a significant association, after correcting for multiple hypothesis testing. From there, additional computational (and often experimental) analyses may fine map the locus to identify a credible set of actually-causal variants, or leverage additional datasets (e.g. epigenomic and gene expression datasets) to glean insights into the molecular mechanisms underlying the association.

In this example, we focus on the use case of a researcher performing a GWAS on coronary artery disease (CAD) - although essentially the same flow could be used for GWAS of any phenotype. We also focus on GWAS using whole genome sequencing (WGS) genotypes, not those obtained from older microarray technology. Using WGS greatly expands the set of variants that can be analyzed - potentially to hundreds of millions - but this, in turn, brings challenges of scalability.

Issues of WGS scale also challenge the way that data is accessed and analyzed. Using microarray data it was straightforward to download data to local infrastructure. WGS researchers are increasingly turning to cloud services. To audit researcher's activities on the cloud for compliance with data use agreements, we also need new systems for tracking which analyses have been run, and by whom.


### Scientific Objective

As a statistical geneticist, I would like to enter my research purpose using a structured ontology and filter down to the list of TOPMed cohorts whose data use restrictions are compatible with my research purpose, so that I know what datasets to apply for access to.

As a statistical geneticist, I would like to apply for access to TOPMed cohorts using a single application form and have it be reviewed by a centralized IRB.
As a statistical geneticist, I would like to search through TOPMed (filtered by data use) and identify all individuals that have coronary artery disease. I would like to build a synthetic cohort from this search and push it to a workspace where I can perform analyses on it.

As a statistical geneticist, I would like to launch a variant calling pipeline across my synthetic cohort to produce a new variant call set, so that it is consistent with other variant call sets that I have utilized previously.
As a statistical geneticist, I would like to upload my own private datasets to the workspace and form a joint-call set with my synthetic cohort from TOPMed.
As a statistical geneticist, I would like to open a Jupyter notebook and perform a GWAS on these samples, carefully controlling for stratification and other forms of artifact. I would then like to identify genomic loci that are genome-wide significant and pull the variants from these loci into a separate data frame.
As a statistical geneticist, I would like to leverage GTEx and ENCODE datasets to identify eQTLs within the loci that are genome-wide significant, as well as look at annotations for these loci.