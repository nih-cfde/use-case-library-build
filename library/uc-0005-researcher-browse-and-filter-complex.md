---
layout: default
title: UC0005 Researcher Browse and Filter- complex
nav_order: 5
parent: Use Cases
has_children: false
---
# Use Case UC0005 Researcher Browse and Filter- complex

**Persona:** [Clinical Researcher](../personas/clinical-researcher.md)

**Objective:** [Multiple DCC Comparison](../objectives/multi-dcc-comparison.md)

### Summary

Pam would like to use the CFDE interface to explain their preliminary results as they writes their next grant. They have preliminary data from a GWAS study performed in their lab that GeneX, a transcription factor, is implicated in Focal Cortical Dysplasia (FCD) and want to know what additional information is available from the Common Fund data sets.
Pam wants to build a table of the summarized metadata and summary statistics
from each RNA-Seq dataset in the Common Fund that relates to Focal Cortical Dysplasia.


Pam logs on to the CFDE interface and searches for brain data, and then filters the results to those studies that used RNASeq on the cerebral cortex. They then search within these results
for "FCD" or "Focal Cortical Dysplasia".
Their initial search with cerebral cortex identifies GTEx and HuBMAP as containing information about gene expression in the cortex. Searching with FCD identifies Kids First cohorts that included this clinical finding. Pam follows links to the GTEx site, and quickly confirms that GeneX is expressed in the cerebral cortex. They then use the HuBMAP datasets identified by their search to examine expression of GeneX and the other genes in finer detail and discovers that GeneX is exclusively expressed in Cajal–Retzius cells in the cerebral cortex. Pam notes the additional data types available, number of participants, and age ranges and consent data for the relevant studies.

Using links in these search results, Pam accesses the Program
page for each dataset and requests access to the ones that fit their needs. They also send
their final table to their postdoc, Lacey, who will do the actual analysis.


### User Tasks

-   [T0001 Access CFDE interface](../user-tasks/t0001-access-cfde-interface.md)
-   [T0006 Search/filter data sets by anatomic terms](../user-tasks/t0006-searchfilter-data-sets-by-anatomic-terms.md)
-   [T0005 Search/filter data sets by type terms](../user-tasks/t0005-searchfilter-data-sets-by-type-terms.md)
-   [T0004 Search within dataset descriptions](../user-tasks/t0004-search-within-dataset-descriptions.md)
-   [T0010 Visualize a table of all projects that match query](../user-tasks/t0010-visualize-a-table-of-all-projects-that-match-query.md)
-   [T0002 Explore Program links](../user-tasks/t0002-explore-program-links.md)
-   [T0003 Export a file of results](../user-tasks/t0003-export-a-file-of-results.md)

### Requirements

#### T0001 Access CFDE interface

-   [R00001 The interface will support GUI web access to end users](../requirements/r00001-the-interface-will-support-gui-web-access-to-end-users.md)
-   [R00002 The interface will support user authentication](../requirements/r00002-the-interface-will-support-user-authentication.md)

#### T0006 Search/filter data sets by anatomic terms

-   [R00003 The interface will support the selection of an Uberon term of interest](../requirements/r00003-the-interface-will-support-the-selection-of-an-uberon-term-of-interest.md)
-   [R00004 The C2M2 model will support information relating Uberon terms to CF programs](../requirements/r00004-the-c2m2-model-will-support-information-relating-uberon-terms-to-cf-programs.md)
-   [R00005 The catalog will store information relating Uberon terms to CF programs](../requirements/r00005-the-catalog-will-store-information-relating-uberon-terms-to-cf-programs.md)


#### T0013 Search/filter data sets by disease terms

-   new requirements: support disease terms
-   new requirements: mechanism to determine user access rights to controlled
-   new requirements: CFDE is allowed to host controlled metadata
-   new requirements: Deriva ATO to display controlled metadata

#### T0005 Search/filter data sets by type terms

-   [R00006 The interface will support the selection of an assay type term of interest](../requirements/r00006-the-interface-will-support-the-selection-of-an-assay-type-term-of-interest.md)
-   [R00007 The C2M2 model will support information relating assay types to CF programs](../requirements/r00007-the-c2m2-model-will-support-information-relating-assay-types-to-cf-programs.md)
-   [R00008 The catalog will store information relating assay types to CF programs](../requirements/r00008-the-catalog-will-store-information-relating-assay-types-to-cf-programs.md)
-   [R00010 The catalog will store information relating projects to CF programs](../requirements/r00010-the-catalog-will-store-information-relating-projects-to-cf-programs.md)
-   [R00011 The C2M2 model will support information relating projects to CF programs](../requirements/r00011-the-c2m2-model-will-support-information-relating-projects-to-cf-programs.md)


#### T0004 Search within results

-   [R00009 The interface will support free text search of results](../requirements/r00009-the-interface-will-support-free-text-search-of-results.md)

#### T0010 Visualize a table of all projects that match query

-   [R00012 The interface will render tables and plots to display filtered data](../requirements/r00012-the-interface-will-render-tables-and-plots-to-display-filtered-data.md)
-   new requirements support number of participants
-   new requirements support age ranges
-   new requirements: The C2M2 supports consents or other information necessary to limit data discovery based on DCC guidelines
-   new requirements: Catalog implementing authorization verification according to DCC guidelines
-   new requirements: Secure CFDE CC cloud system hosting catalog, interface, and other services

#### T0002 Explore Program links

-   [R00013 The interface will support links to original data sources within the results](../requirements/r00013-the-interface-will-support-links-to-original-data-sources-within-the-results.md)

#### T0003 Export a file of results

-   [R00014 The interface will support end user download of tables and figures in common formats](../requirements/r00014-the-interface-will-support-end-user-download-of-tables-and-figures-in-common-formats.md)
