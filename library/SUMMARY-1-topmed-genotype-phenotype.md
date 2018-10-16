---
title: TOPmed Genotype-Phenotype Association Testing
narratives:
- NARRATIVE-1
tags:
- topmed genotype-phenotype
---
**Scenario**

Geraldine is a biomedical researcher who wants to look for genetic variants
associated with coronary artery disease (CAD) by performing Genome Wide
Association Analysis (GWAS), using genotypes from whole genome sequence (WGS).
A large sample size is needed for statistical power to detect effects on a
complex trait such as CAD. This sample size can be achieved only by harmonizing
and combining data across multiple studies.  WGS provides hundreds of millions
of variants to test, so powerful computing resources are also required.
Furthermore, Geraldine wants to collaborate on this project with a team of
investigators who have expertise in various aspects of CAD, so needs a mechanism
for sharing human subjects data.


**Current Approach**

Without the Commons, Geraldine would have to find and download several datasets
to build a large synthetic cohort. It is likely that different studies would
have annotated their data differently, making it difficult to identify data
elements representing relevant aspects of CAD. Geraldine would need to spend a
considerable amount of time searching data repositories and identifying
appropriate variables because, for example, one study may name the relevant
variable as CAD and another as atherosclerosis. Geraldine would also need to
find a large computing resource to run the analysis and to install and run a
number of command line programs. She would need to obtain permission to access
the relevant data sets and download large data files containing the WGS data.
Because the data are from human subjects, and require controlled access, they
cannot readily be shared with collaborators.

**With the Data Commons Phase I**

Geraldine logs into her favorite full stack and searches for dbGaP studies with
WGS-genotypes and CAD phenotypes.  She is able to find CAD-related phenotypes in
multiple studies, even though they use different variable names and
descriptions, because the search process uses biomedical ontologies, natural
language processing and other sophisticated tools.  She obtains dbGaP approvals
for these data sets (through the existing dbGaP mechanism) and is able to access
the files within the Data Commons, eliminating the need for large file
transfers.  She has a workspace within which she can share data and results with
her collaborators (who have the same access permissions).  She can run her
analysis using a pre-built and cost-efficient workflow.  She and her
collaborators can plot and summarize their results interactively within their
workspace using a Jupyter notebook.

**With Data Commons longer vision:**

Geraldine now has the ability to search many more data repositories to find
CAD-related studies.  When she finds new studies, she is able to apply for
access easily using a Data Commons interface, which prompts her for the
necessary information.  Her approvals arrive much faster than before due to
automation of data access processes, and she is able guide her collaborators to
efficiently obtain compatible approvals. Large-scale harmonization of the
phenotype metadata have been done so that searches for CAD-related phenotypes
have better sensitivity and specificity, thus facilitating the construction of
her cross-study data set.  She now has a large suite of pre-built applications
and workflows to choose from for her analysis.