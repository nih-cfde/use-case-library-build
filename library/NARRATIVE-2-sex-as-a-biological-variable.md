---
title: Sex as a Biological Variable
persona: PERSONA-1-biological-data-scientist
blurb: Sexual dimorphism refers to differences between males and females of the same species. We will use AGR and GTEx to understand some aspects of the differences between male and female biology at a genome scale.
epics:
- EPIC-8
- EPIC-9
- EPIC-10
- EPIC-11
- EPIC-12
tags:
- AGR
- GTEx
- biological
- dimorphism refers
- female biology
- genome scale
- sex
---
Sexual dimorphism is the term that refers to differences between males
and females of the same species. In medicine, we study sex and gender
medicine with the goal of understanding fundamental differences of
biology and behaviour between women and men in order to improve health
care for both sexes by tailoring diagnostic, screening, and treatment
strategies for men and women. Our specific hypothesis in the pilot
phase of the NIH Data Commons project is that we can use the model
organism data resources in the Alliance of Genomic Resources and the
tissue-based gene expression data in the Genotype-Tissue Expression
(GTEx) project to understand some aspects of the differences between
male and female biology at genome scale. An additional hypothesis is
that we can use this information to inform our analysis of male and
female participants in the TOPMed project. The following two example
projects will exemplify the approach taken to model organism and GTEx
data.

### Scientific Objective

Scientific Objective #1: We want to investigate phenotypic differences
across male and female animals in large-scale screening programs of
genetically modified animals. We aim to perform an analysis across the
entire phenome using an ontology-based analysis. Phenotype ontologies
are used to describe phenotypic outcomes of knockouts and other
genetic modifications of genes in model organisms such as mouse, rat,
zebrafish, xenopus, drosophila, C. elegans, and yeast. We'll want to
generate a table of results for each ontology term with chi-square
statistics, p-values, and corrected p-values; to determine the
correlation of distributions of phenotypes in organ systems with
expression of genes in the organs; and to generate a table of GO or
other pathway analysis terms that characterize the sexually dimorphic
phenotypes or gene expressions.