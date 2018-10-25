---
title: Construct a multi-species phenotype dataset.
blurb: Construct a multi-species phenotype dataset.
user-stories:
- USERSTORY-40
- USERSTORY-41
- USERSTORY-42
- USERSTORY-43
tags:
- multi-species phenotype dataset
---
a. The analysis challenge is currently that each of the MODs using
different file formats and semantics to record phenotypic data, and
not all MODs record sex-specific annotations. There are challenges
related to proper interpretation of file formats and assumptions, for
instance, what to do if multiple genes are recorded for a model. This
requires deep understanding of the underlying data and communication
with the MOD databases. In practical terms, we require all of the data
to be put into a flexible computational datastructure that allows
ontology traversals and statistical tests.

b. Harmonize data across available datasets. For instance, for mouse
dimorphism data there are two substantial resources, from MGI and the
IMPC, that use different formats. It should be possible to test either
dataset alone or to combine them.
