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
- t-0031
- t-0032
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
- r-00042
- r-99999
- r-00043
- r-00044
---


Jordan is a Data Administrator for a Common Fund Data Coordinating Center. They need
to provide a description of the Data Coordinating Center’s data to the CFDE so that:
(a) the data can be discovered by clinical researchers, (b) the data can be compared
with data from other Data Coordinating Centers, and (c) they and others can see how
CFDE’s metrics, statistics, and FAIRness measurements apply to the data. We assume
Jordan has previously been registered with CFDE and authorized by their Data
Coordinating Center to act as a data administrator on its behalf.

Jordan first reviews the documentation for the C2M2 data model and then follows a tutorial for
submitting data to the CFDE portal. If they have not
previously installed CFDE’s ingest tool, they do so. They then extract the required
metadata from their Data Coordinating Center’s data and transform it into the C2M2
data model. Once the metadata is in the C2M2 model, they run CFDE’s submission tool to
submit the metadata. When the submission completes, Jordan accesses the CFDE interface
and views the results in a non-public reviewing view. If the results are not
satisfactory, they adjust the metadata and re-run the ingest tool, repeating until
the results are satisfactory. He can consult the documentation or CFDE support for help resolving errors.

If the results are satisfactory, they approves the data
release and it is marked for review by CFDE personnel. As necessary, Jordan now knows how to submit subsequent metadata manifests for comparison.



<!-- some details to add:

Data administrator: uses the CFDE Submission Tool to make a Data Submission

A data administrator or their designee should be able to:

DONE t-0013 - is this C2M2 documentation
    - Consult documentation about building their metadata manifest

DONE assuming this is a tutorial of the data submission process - t-0031
    - Follow a minimal example/tutorial for building a metadata manifest

DONE this still sounds like C2M2 documentation - t-0013
    - Consult technical documentation for in depth model information

DONE t-0015
    - Submit a metadata manifest into the submission tool

DONE r-00025 - a req of t-0015
    - Be authenticated as an approved data submitter

DONE r-00028 - a req of t-0015
    - Be notified of errors that make their manifest incompatible with the model

DONE this is a new req (specifically the Globus part) - adding to t-0015 as r-00043
    - Be notified of errors that make their manifest unable to be submitted to the Globus endpoint

DONE this still sounds like C2M2 documentation - t-0013
    - Consult documentation on how to resolve any errors

DONE this is new - t-0032
    - Be able to contact CFDE support if they cannot resolve errors

DONE this looks like new req for t-0015. r-00044
    Receive notification of successful submission of the manifest

DONE this is a new task? or just starting the process over? not sure what feature allows comparison of datasets - not going to make this a separate task yet.
    Submit subsequent metadata manifests for comparison -->
