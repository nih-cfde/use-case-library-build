---
title: Governance and Audits
narratives:
- NARRATIVE-12
tags:
- audits
- governance
---
**Scenario:**

Sarah, who represents a Governance Authority (the Authority), is performing a security audit on a resource in the Data Commons. She is interested in how datasets are being used by researchers, and whether data use is a good fit for the statement of research purpose for a study.

**Current approach:**

Sarah would need to manually curate a list of researchers or data sets to audit, then cross-check usage by hand.

**With Data Commons Phase 1:**

Sarah can obtain machine generated data access records for datasets by GUID, and look up research statements for researchers who accessed it.

**With Data Commons longer vision:**

Sarah accesses the Data Commons user interface for querying the audit trail. The user interface allows her to specify her search criteria, potentially including an assertion that her query is being made with elevated permissions, for system security purposes. Her search criteria include the GUID of resource, as well as the start date and end date of the time window of interest. The data returned contains all relevant details from the ledger including the UIDs of the users who performed each activity and any updating entries to the activity records in the audit trail that contain risk assessment scores for particular activities. The data returned may not contain certain data elements that are used by the system for its internal processing.

Data use limitations for each dataset are expressed in machine-readable standard form (i.e., expressed using a standardized ontology), there is a machine-readable standard statement of research purpose accompanying each (human-readable application for access to data), and an algorithm compares the data use restrictions to the researcher’s purpose and lets her know whether the two are compatible and if manual review is required.