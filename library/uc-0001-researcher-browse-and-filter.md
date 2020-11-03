---
layout: default
title: "UC0001 Researcher Browse and Filter &#x2705; "
nav_order: 1
parent: Use Cases
completed: June 2020
has_children: false
---

# Use Case UC0001 Researcher Browse and Filter

**Completed:** June 2020

**Persona:** [Clinical Researcher](../personas/clinical-researcher.md)

**Objective:** [Multiple DCC Comparison](../objectives/multi-dcc-comparison.md)

### Summary

Pam wants to build a table of the summarized metadata and summary statistics
from each RNA-Seq dataset in the Common Fund that relates to Focal Cortical Dysplasia.

Pam logs on to the CFDE interface and searches for brain data, and then filters the results to those studies that used RNASeq. They then search within these results
for "FCD" or "Focal Cortical Dysplasia".
Their initial search with cerebral cortex identifies GTEx and HuBMAP as containing information about gene expression in the cortex. Searching with FCD identifies KidsFirst addtional cohorts that included this clinical finding.

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


#### T0006 Search/filter data sets by anatomic terms

-   [R00003 The interface will support the selection of an Uberon term of interest](../requirements/r00003-the-interface-will-support-the-selection-of-an-uberon-term-of-interest.md)
-   [R00004 The C2M2 model will support information relating Uberon terms to CF programs](../requirements/r00004-the-c2m2-model-will-support-information-relating-uberon-terms-to-cf-programs.md)
-   [R00005 The catalog will store information relating Uberon terms to CF programs](../requirements/r00005-the-catalog-will-store-information-relating-uberon-terms-to-cf-programs.md)


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

#### T0002 Explore Program links

-   [R00013 The interface will support links to original data sources within the results](../requirements/r00013-the-interface-will-support-links-to-original-data-sources-within-the-results.md)
-   [R00032 The C2M2 model will support links to original data sources](../requirements/r00032-the-c2m2-model-will-support-links-to-original-data-sources.md)
-   [R00033 The catalog will links to original data sources](../requirements/r00033-the-catalog-will-links-to-original-data-sources.md)

#### T0003 Export a file of results

-   [R00014 The interface will support end user download of tables and figures in common formats](../requirements/r00014-the-interface-will-support-end-user-download-of-tables-and-figures-in-common-formats.md)
