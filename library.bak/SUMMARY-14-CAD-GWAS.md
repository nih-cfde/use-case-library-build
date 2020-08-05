---
title: Coronary Artery GWAS Summary
narratives:
- NARRATIVE-14
tags:
- coronary artery gwas summary
---
**Scenario**

Airyonna is a statistical geneticist, and she is interested in using statistical methods to identify genetic risk factors for coronary artery disease. As Airyonna has never worked with patients directly, she has decided to start by using genotype-phenotype association testing on existing biomedical data sets. However, while Airyonna has the mathematical background to perform and interpret this analysis, she does not have easy access to a computing cluster, and has only basic coding skills. Similarly, while Airyonna will likely have little trouble getting approval for her experiment, she does not currently have access to any human genomics datasets, and is unsure how to find them or apply for access.


**Current Approach**

Currently, Airyonna would likely need to find a mentor to walk her through the process of applying for data access, and would likely find the process of locating suitable datasets frustrating. Every data set has varying use conditions and sets of variables that were collected, however it's not always possible to tell whether a given dataset can be used in her analysis without being approved for access. Airyonna might spend several months finding potential data and applying for access only to find that it is poorly suited to her study. Once she has a cohort of datasets, Airyonna would also have to find computational resources for running her analysis, and would likely have to devote a substantial amount of time to learning a programming language like R or Python.


**With the Data Commons Phase I**



**With Data Commons longer vision:**

Airyonna can log into the Data Commons and navigate datasets using a structured ontology. She can filter down to a list of TOPMed cohorts whose data use restrictions are compatible with her research purpose and report her desired variables. She will only need to apply for access to these datasets, and can use a single application form which will be reviewed by a centralized IRB. Once she has access, Airyonna can identify all the individuals in her data that have coronary artery disease and build a synthetic cohort. She can push this data to a workspace in the cloud where she can perform analyses on it.

For her analysis, Airyonna can launch a variant calling pipeline across her synthetic cohort to produce a new variant call set. If she finds a new dataset she would like to add later, she can easily come back to this step, so that any new data is consistent with other variant call sets that she used previously. Similarly, if she has any, Airyonna can also upload her own private datasets to this workspace and form a joint-call set with my synthetic cohort from TOPMed.
Once she has a collection of variants, Airyonna can open a Jupyter notebook and perform a GWAS anaylsis on these samples. The notebook is pre-written, so she can carefully control for stratification and other forms of artifacts even though she only knows enough Python to make small edits to the code. Using this notebook, she can identify genomic loci that show genome-wide  signifigance, and pull the variants from these loci into a separate data frame. Finally, Airyonna can leverage GTEx and ENCODE datasets to identify eQTLs within the loci that show genome-wide significance, as well as look at annotations for these loci.