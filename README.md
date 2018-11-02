# Use Case Library

This GitHub repository contains the Markdown materials behind the NIH Data Commons Use Case Library, which is accessible at <http://nih-data-commons.us/use-case-library/>.

The Use Case Library provides a set of high-level summaries that capture the essential scientific objectives and place them in the context of larger goals and the Data Commons Pilot Phase Consortium timeline. The Use Case Library also consists of a set of user narratives that capture highly-related scientific objectives for biomedical research that can be achieved by a series of technically-focused user epics and stories. A detailed description of the structure the Use Case Library can be found in the [glossary](./templates/glossary.md)

## How to contribute new contents

We welcome new contributions. 
Please read the [contributor guidelines](./templates/CONTRIBUTING.md) before submitting a pull request. 

## A brief overview of how the site its built

The files in `library/` define a collection of high-level summaries,
user summaries, personas, narratives, user epics, and user stories.

These files provide three types of information:
* a unique identifier, given by the TYPE-NUMBER in the filename; so `SUMMARY-1-topmed-genotype-phenotype` has the identifier `SUMMARY-1`.
* some metadata, stored in the YAML header at the top of the file contents; this metadata links between object types.
* markdown content describing things in more detail.

The script `scripts/process.py` loads all of these files in, checks
the metadata for correctness, and then creates a collection of output
markdown files for a [mkdocs site](https://www.mkdocs.org/) under
`output/docs`. The mkdocs configuration file is `output/mkdocs.yml`.
These markdown files are created using jinja2 templating under the
directory `templates/

[mkdocs](https://www.mkdocs.org/) then takes `output/docs/` and
`output/mkdocs.yml` and builds the mkdocs site, which is static HTML
that can be viewed or deployed.  The static site is located at
`output/site/`, and `output/site/index.html` is the main entry point.