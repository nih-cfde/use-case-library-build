---
title: Project Setup - sex as a biological variable
blurb: Acquire accounts and access to AGR and GTEx resources; and plan statistical analysis
user-stories:
- USERSTORY-1
- USERSTORY-2
- USERSTORY-5
tags:
- AGR
- GTEx
- acquire
- project setup
- statistical analysis
---
a. We aim to perform an analysis across the entire phenome using an
ontology-based analysis. Phenotype ontologies are used to describe
phenotypic outcomes of knockouts and other genetic modifications of
genes in model organisms such as mouse, rat, zebrafish, xenopus,
drosophila, C. elegans, and yeast. The first step is to import all of
this data into an integrated ontology analysis framework. In some
situations it may be desired to analyze quantitative data (e.g., IMPC
mouse data).

b. We decide on a statistical analysis procedure. One standard
approach involves counting the genes/models that are associated with
individual ontology terms. In general, the “annotation propagation
rule” should be followed, which states that annotations to ontology
terms are “inherited” up is_a relations. We can then perform this
separately for male and female organisms, and perform a chi-squared or
Fisher exact test for each ontology term.