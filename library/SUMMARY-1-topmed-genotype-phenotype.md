---
title: TOPmed Genotype-Phenotype Association Testing
narratives:
- NARRATIVE-1
---

**Scenario**

Geraldine is a biomedical researcher wants to look for genetic variants associated with a human disease by using Genome Wide Association Analysis (GWAS). However, GWAS is a complicated statistical technique, so finding causal variants for a complex disease will require both a lot of statistical power and well annotated metadata. In addition, running a GWAS analysis on the human genome will require a great deal of compute power and time.

**Current Approach**

Without the Commons, Geraldine would have to find and download several datasets to find enough cases and controls. Likely, these studies would have been done by different researchers, and so would have data about different variables. Geraldine would need to spend a considerable amount of time reading papers and data repositories to find studies that match her cohort requirements, and then manually curate the metadata of these studies before she could combine them, for instance, noticing that one study referred to a variable as 'gender' where another used 'sex'. Geraldine would also need to find a large computing resource to run her analysis, as it will take several weeks on her laptop, and she will need to install and understand how to run a number of command line programs the analysis relies on.

**With the Data Commons Phase I**

Geraldine logs into her favorite full stack and searches for people with the disease, and age range of interest, as well as matched controls. She finds five studies that match all her requirements and that already have harmonized metadata. She can easily export them to a workspace in the cloud and run her analysis using a pre-built workflow.
