---
title: Create a Data Release
completed:
tutorial:
goal: Support the storage, sharing, and sustainability of CF data sets
persona:
- p-003
objective:
- obj-0002
user_tasks:
- t-0017
- t-0013
- t-0014
- t-0015
- t-0016
requirements:
- r-00001
- r-00002
- r-00004
- r-00007
- r-00011
- r-00016
- r-00019
- r-00022
- r-00023
- r-00024
- r-00025
- r-00026
- r-00027
- r-00028
- r-00029
- r-00030
- r-00031
- r-00037
---



Jordan is a Data Administrator for a Common Fund Data Coordinating Center. They need
to provide a description of the Data Coordinating Center’s data to the CFDE so that:
(a) the data can be discovered by clinical researchers, (b) the data can be compared
with data from other Data Coordinating Centers, and (c) they and others can see how
CFDE’s metrics, statistics, and FAIRness measurements apply to the data. We assume
Jordan has previously been registered with CFDE and authorized by their Data
Coordinating Center to act as a data administrator on its behalf.

Jordan first reviews the documentation for the C2M2 data model. If they have not
previously installed CFDE’s ingest tool, they do so. They then extract the required
metadata from their Data Coordinating Center’s data and transform it into the C2M2
data model. Once the metadata is in the C2M2 model, they run CFDE’s submission tool to
submit the metadata. When the submission completes, Jordan accesses the CFDE interface
and views the results in a non-public reviewing view. If the results are not
satisfactory, they adjust the metadata and re-run the ingest tool, repeating until
the results are satisfactory. If the results are satisfactory, they approves the data
release and it is marked for review by CFDE personnel.
