---
title: GTEx - Sharing Raw Data
narratives:
- NARRATIVE-3
---

**Scenario**

Mamie wants to use existing raw data on GTEx as input for evaluating a new computational method.

**Current Approach**

Once Mamie had gained access rights to GTEx, she would retrieve raw data files. However, she'd have to manually match the IDs used in the paper where the raw data originated to the GTEx dataset IDs. Furthermore if there was an update to the GTEx before Mamie finished her analysis, the paths to the raw data could change and need to be manually re-matched to the IDs.

**With the Data Commons Phase I**

Mamie can log into the GTEx portal and use a simple interface to
select data cohorts and export them to a workspace in FireCloud. Once
her data is selected, Mamie is given a table that maps sample IDs
to static raw data paths.

**With Data Commons longer vision:**

Mamie can develop new methods for variant discovery, and submit her workflow
to the Data Commons as CWL. The ability to share both data and pipelines
within the Commons makes research faster for others, but also allows non-experts
to run workflows that they otherwise would not have been able to code.
