---
title: GTEx - Sharing Raw Data
narratives:
- NARRATIVE-3
---
**Scenario**

Mamie wants to use existing raw data on GTEx to use as input for evaluating a new computational method

**Current Approach**

Once Mamie has gained access rights to GTEx, she could retrieve raw
data files. However, she'll have to manually match the IDs used in the
papers she used to choose these datasets to the GTEx IDs. Furthermore
if there is an update to the GTEx before Mamie finishes her analysis,
the paths to the raw data may change and need to be manually
re-matched to the IDs

**With the Data Commons Phase I**

Mamie will log into the GTEx portal and use a simple interface to
select data cohorts and export them to a workspace in FireCloud. Once
her data is selected, Mamie will be given a table that maps sample IDs
to static raw data paths

**With Data Commons longer vision:**

Mamie might develop new methods for variant discovery, and submit her workflow
to the Data Commons as a CWL. The ability to share both data and pipelines
within the Commons makes research faster for others, but also allows non-experts
to run workflows that they otherwise would not have been able to code.