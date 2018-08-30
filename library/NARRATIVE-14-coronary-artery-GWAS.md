---
title: Coronary Artery GWAS User Narrative
persona: PERSONA-7-statistical-geneticist
blurb: Identify genetic risk factors for coronary artery disease.
epics:
- EPIC-18
- EPIC-7 
- EPIC-8 
---

### Scientific Objective 

Genome-wide association studies (GWAS), where variants across the genome are tested for association with a phenotype of interest, are widely used in human genetics research. The primary output of these studies is the identification of genetic loci that have a significant association, after correcting for multiple hypothesis testing. From there, additional computational (and often experimental) analyses may fine map the locus to identify a credible set of actually-causal variants, or leverage additional datasets (e.g. epigenomic and gene expression datasets) to glean insights into the molecular mechanisms underlying the association.

In this example, we focus on the use case of a researcher performing a GWAS on coronary artery disease (CAD) - although essentially the same flow could be used for GWAS of any phenotype. We also focus on GWAS using whole genome sequencing (WGS) genotypes, not those obtained from older microarray technology. Using WGS greatly expands the set of variants that can be analyzed - potentially to hundreds of millions - but this, in turn, brings challenges of scalability.

Issues of WGS scale also challenge the way that data is accessed and analyzed. Using microarray data it was straightforward to download data to local infrastructure. WGS researchers are increasingly turning to cloud services. To audit researcher's activities on the cloud for compliance with data use agreements, we also need new systems for tracking which analyses have been run, and by whom.

