---
title: GTEx Analysis with BioJupies
narratives: 
- NARRATIVE-24 
tags:
- Biojupies
- GTEx analysis
---
**Scenario**

Ramon wants to use explore data from the Genotype-Tissue Expression (GTEx) database to look at genes whose expression levels correlate with several phenotypes he studies. Although Ramon is familiar with the overall process and biology of RNAseq analysis, he is unfamiliar with the computational and statistical aspects, and is unsure how to get started. Ideally, he would like to run a quick, standard analysis that outputs easy to interprete results, so he can screen his phenotypes without spending a lot of time learning new techniques. Ramon also doesn't have access to a large computing center, which makes running large complex analyses difficult.

**Current Approach**

Once Ramon searched the GTEx database to find the samples he was interested in, he would have to find a cloud resource or space on his personal computer to store the data. He would have to learn at least one programming language in order to run an anaylsis pipeline, and another language to plot the results in an intuitive way. As Ramon is a computer novice, this analysis will likely take several years of learning programming, statistics, and modeling techniques.

**With the Data Commons Phase I**

Ramon can use the new BioJupies GTEx interface to search the available metadata and choose samples with his phenotype of interest and a suitable control. The tissue sample IDs from the his selection are then passed to the BioJupies API for downstream analysis. This will automaticaly create a Jupyter Notebook, which includes an interactive PCA (Principle Components Analysis) and Clustergrammer plots, as well as enrichment analysis and small molecule predictions. By connecting through this interface, Ramon can run an in-depth, rapid exploration of a large and complex dataset to facilitate hypothesis generation, without any programming knowledge.

**With Data Commons longer vision:**
