# Use Case Library

This GitHub repository contains the Markdown materials behind the NIH Data Commons Use Case Library, which is accessible at <http://nih-data-commons.us/use-case-library/>.

The Use Case Library provides a set of high-level summaries that capture the essential scientific objectives and place them in the context of larger goals and the Data Commons Pilot Phase Consortium timeline. The Use Case Library also consists of a set of user narratives that capture highly-related scientific objectives for biomedical research that can be achieved by a series of technically-focused user epics and stories. A detailed description of the structure the Use Case Library can be found in the [glossary](./templates/glossary.md).

## How to contribute new content

We welcome new contributions. 
Please read the [contributor guidelines](./templates/CONTRIBUTING.md) before submitting a pull request. 

## A brief overview of how the site its built

The Markdown files in `library/` define a collection of high-level use case
library items: summaries, personas, narratives, user epics, and user stories.

These files provide three types of information:

* a **unique identifier**, given by the TYPE-NUMBER in the filename; so `SUMMARY-1-topmed-genotype-phenotype` has the identifier `SUMMARY-1`.
* **metadata**, stored in the YAML header at the top of the file contents; this metadata links between object types.
* **markdown content** describing the library item in more detail.

The script `scripts/process.py` processes each library item, 
checking the content of the item and assembling links to other library
items, and uses templates to build an [mkdocs](https://www.mkdocs.org/)-ready
static site in `output/docs/`, with the mkdocs configuration file at `output/mkdocs.yml`.
The processing step uses Jinja for templating (see `templates/` directory).

The use case library static site is built from the automatically-generated
mkdocs site materials. The result is static HTML that can be deployed on
a web server served or using Github Pages. The final static site files are
located in `output/site/`. The file  `output/site/index.html` is the main
entry point.

## A more detailed guide to building the site

See the [Contributing](http://nih-data-commons.us/use-case-library/CONTRIBUTING/)
page for more detailed information about building the Use Case Library.

