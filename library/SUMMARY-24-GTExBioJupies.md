---
title: GTEx Analysis with BioJupies
narratives: null
tags:
- Biojupies
- gtex analysis
---
The Genotype-Tissue Expression (GTEx) project aims to create a better understanding of the relationship between genetic variation and tissue-specific gene expression. The BioJupies GTEx interface facilitates exploratory data analysis of the RNA-seq data collected for the GTEx project, which contains thousands of tissue samples from hundreds of donors. Through an interactive user interface, BioJupies displays metadata elements to select two groups of samples to compare. The tissue sample IDs from the metadata are used to extract the gene expression data for each sample, which are passed to the BioJupies API for downstream analysis. The resultant Jupyter Notebook, automatically created by BioJupies, includes interactive PCA and Clustergrammer plots, as well as enrichment analysis and small molecule predictions. By connecting the GTEx RNA-seq data with BioJupies, we enable in-depth rapid exploration of a large and complex dataset to facilitate hypothesis generation.