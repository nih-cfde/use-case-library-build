---
title: Sex as a Biological Variable
persona: PERSONA-1-biological-data-scientist
blurb: Sexual dimorphism is the term that refers to differences between males and females of the same species. In medicine, we study sex and gender medicine with the goal of understanding fundamental differences of biology and behaviour between women and men in order to improve health care for both sexes by tailoring diagnostic, screening, and treatment strategies for men and women.
Our specific hypothesis in the pilot phase of the NIH Data Commons project is that we can use the model organism data resources in the Alliance of Genomic Resources and the tissue-based gene expression data in the Genotype-Tissue Expression (GTEx) project to understand some aspects of the differences between male and female biology at genome scale. An additional hypothesis is that we can use this information to inform our analysis of male and female participants in the TOPMed project. 
The following two example projects will exemplify the approach taken to model organism and GTEx data.

epics:
- EPIC-1
- EPIC-2
- EPIC-3
- EPIC-4
- EPIC-5
- EPIC-6
- EPIC-7
---

### Scientific Objective 

TScientific Objective #1: Investigate phenotypic differences across male and female animals in large-scale screening programs of genetically modified animals.
Develop an analysis plan for phenotype analysis
We aim to perform an analysis across the entire phenome using an ontology-based analysis. Phenotype ontologies are used to describe phenotypic outcomes of knockouts and other genetic modifications of genes in model organisms such as mouse, rat, zebrafish, xenopus, drosophila, C. elegans, and yeast. The first step is to import all of this data into an integrated ontology analysis framework. In some situations it may be desired to analyze quantitative data (e.g., IMPC mouse data).
We decide on a statistical analysis procedure. One standard approach involves counting the genes/models that are associated with individual ontology terms. In general, the “annotation propagation rule” should be followed, which states that annotations to ontology terms are “inherited” up is_a relations. We can then perform this separately for male and female organisms, and perform a chi-squared or Fisher exact test for each ontology term.
Construct an analysis-ready data set
The analysis challenge is currently that each of the MODs using different file formats and semantics to record phenotypic data, and not all MODs record sex-specific annotations. There are challenges related to proper interpretation of file formats and assumptions, for instance, what to do if multiple genes are recorded for a model. This requires deep understanding of the underlying data and communication with the MOD databases. In practical terms, we require all of the data to be put into a flexible computational datastructure that allows ontology traversals and statistical tests. 
Harmonize data across available datasets. For instance, for mouse dimorphism data there are two substantial resources, from MGI and the IMPC, that use different formats. It should be possible to test either dataset alone or to combine them
Integrate other relevant data. It should be possible to integrate gene expression data from resources such as MGI or BGE. It should also be possible to integrate functional and pathway data from resources such as Gene Ontology (GO).
Perform and visualize analysis
Generate a table of results for each ontology term with chi-square statistic, p-value, corrected p-value.
Generate correlation of distribution of phenotype in organ systems with expression of genes in the organs. 
Generate table of GO or other pathway analysis terms that characterize the sexually dimorphic phenotypes or gene expressions.
