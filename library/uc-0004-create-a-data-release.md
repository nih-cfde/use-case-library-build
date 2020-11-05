---
layout: default
title: UC0004 Create a Data Release
nav_order: 4
parent: Use Cases
has_children: true
---
# Use Case UC0004 Create a Data Release

**Persona:** [Data Administrator](../personas/data-administrator.md)

**Objective:** [Create a Data Release](../objectives/create-data-release.md)

# Summary

Jordan is a Data Administrator for a Common Fund Data Coordinating Center. They need
to provide a description of the Data Coordinating Center’s data to the CFDE so that:
(a) the data can be discovered by clinical researchers, (b) the data can be compared
with data from other Data Coordinating Centers, and (c) they and others can see how
CFDE’s metrics, statistics, and FAIRness measurements apply to the data. We assume
Jordan has previously been registered with CFDE and authorized by their Data
Coordinating Center to act as a data administrator on its behalf.

Jordan first reviews the documentation for the C2M2 data model. If they have not
previously installed CFDE’s ingest tool, they does so. They then extract the required
metadata from their Data Coordinating Center’s data and transform it into the C2M2
data model. Once the metadata is in the C2M2 model, they run CFDE’s ingest tool to
ingest the metadata. When the ingest completes, Jordan accesses the CFDE interface
and views the results in a non-public reviewing view. If the results are not
satisfactory, they adjust the metadata and re-runs the ingest tool, repeating until
the results are satisfactory. If the results are satisfactory, they approves the data
release and it is marked for review by CFDE personnel.


### User Tasks

-   [T0013 Review C2M2 documentation](../user-tasks/t0013-review-c2m2-documentation.md)
-   [T0014 Install the CFDE ingest tool](../user-tasks/t0014-install-cfde-ingest-tool.md)
-   [T0015 Ingest a candidate data release](../user-tasks/t0015-ingest-candidate-data-release.md)
-   [T0001 Access to CFDE interface](../user-tasks/t0001-access-cfde-interface.md)
-   [T0016 Review and approve/reject ingest results of a candidate data release](../user-tasks/t0016-dcc-review-approve-reject-ingest-results.md)

### Requirements

#### T0013 Review C2M2 documentation

-   [R00004 The C2M2 model will support information relating Uberon terms to CF programs](../requirements/r00004-the-c2m2-model-will-support-information-relating-uberon-terms-to-cf-programs.md)
-   [R00007 The C2M2 model will support information relating assay types to CF programs](../requirements/r00007-the-c2m2-model-will-support-information-relating-assay-types-to-cf-programs.md)
-   [R00011 The C2M2 model will support information relating projects to CF programs](../requirements/r00011-the-c2m2-model-will-support-information-relating-projects-to-cf-programs.md)
-   [R00016 The C2M2 model will support information relating species terms to CF programs](../requirements/r00016-the-c2m2-model-will-support-information-relating-species-terms-to-cf-programs.md)
-   [R00019 The C2M2 model will support information relating FAIR metrics to CF programs](../requirements/r00019-the-c2m2-model-will-support-information-relating-fair-metrics-to-cf-programs.md)
-   [R00022 The C2M2 documentation is publicly available using a standard web browser and internet connection](../requirements/r00022-the-c2m2-documentation-is-publicly-available.md)

#### T0014 Install CFDE ingest tool

-   [R00023 The CFDE ingest tool is publicly available](../requirements/r00023-the-cfde-ingest-tool-is-publicly-available.md)
-   [R00024 The CFDE ingest tool can be installed on a standard Mac, Windows, or Linux workstation or Linux server system](../requirements/r00024-the-cfde-ingest-tool-can-be-installed.md)

#### T0015 Ingest a candidate data release

-   [R00025 The CFDE ingest tool supports user authentication](../requirements/r00025-the-cfde-ingest-tool-supports-user-authentication.md)
-   [R00026 The CFDE ingest tool requires authorization to ingest data for a specific DCC](../requirements/r00026-the-cfde-ingest-tool-requires-authorization.md)
-   [R00027 The CFDE ingest tool can ingest data in the C2M2 data model](../requirements/r00027-the-cfde-ingest-tool-can-ingest-data-in-the-c2m2-data-model.md)
-   [R00028 The CFDE ingest tool rejects malformed C2M2 metadata and provides comprehensible/actionable diagnostics](../requirements/r00028-the-cfde-ingest-tool-rejects-malformed-c2m2-metadata.md)

#### T0001 Access CFDE interface

-   [R00001 The interface will support GUI web access to end users](../requirements/r00001-the-interface-will-support-gui-web-access-to-end-users.md)
-   [R00002 The interface will support user authentication](../requirements/r00002-the-interface-will-support-user-authentication.md)

#### T0016 Review and approve/reject ingest results of a candidate data release

-   [R00029 The interface allows data administrators to review the ingest results for their recent candidate data releases](../requirements/r00029-the-interface-allows-data-administrators-to-review-the-ingest-results.md)
-   [R00030 The interface allows data administrators to approve a recent candidate data release](../requirements/r00030-the-interface-allows-data-administrators-to-approve-a-recent-candidate-data-release.md)
-   [R00031 When a recent candidate data release is approved by the data administrator, the candidate data release is marked for review by CFDE personnel](../requirements/r00031-when-data-release-is-approved-by-data-administrator-it-is-marked-for-review-by-cfde.md)
