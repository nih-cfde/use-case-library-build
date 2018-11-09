---
title: Data preparation
blurb: Extract and harmonize HDL measurements from each individual study data.
user-stories:
- USERSTORY-7
- USERSTORY-8
- USERSTORY-9
tags:
- HDL
- extract
- individual study data
---
This is a messy data extraction problem. For example, some studies may measure HDL at a single point in time, while others may measure across multiple visits, and some may have used different measurement techniques; this becomes both a data extraction problem (how is the data stored in the relevant CSV files?) and also a data harmonization problem (EPIC-24). Some studies may measure using method A, while others may measure using method B; this should be part of the extraction, because it is important for batch correction later on. The question of how a study measures HDL is public metadata on the dbGaP study; the actual HDL values are access-restricted.