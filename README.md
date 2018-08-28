# Use Case Library

## Getting started

(You'll need to install the packages in `requirements.txt`.)

Run:
```
snakemake
```

and then open `output/site/index.html`.

You can see a deployed version at https://dib-lab.github.io/ucl/.

## A brief overview of How This All Works.

The files in `library/` define a collection of high-level summaries,
user narratives, epics, user stories, and personas.

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

## How to contribute new contents

To create a new summary, persona, etc.:

* Make a new branch fom latest master.
* Create a new SUMMARY-, PERSONA-, NARRATIVE-, USERSTORY-, or EPIC-
  file under `library/` by copying an existing file. Make sure that
  the filename specifies a unique ID, e.g. `SUMMARY-1-xyz` yields the
  ID `SUMMARY-1` which is *not* unique.
* Update the YAML metadata at the top of the file to reflect your new metadata.
* Edit the markdown description below the YAML header.
* Build the file using `snakemake`, check the output.
* Iterate until you're happy.
* Add new file to git repo, commit, push.
* Set up a Pull Request to merge into master and tag in @ctb.

## Higher order goals / why we did this:

* stable URL structure and permalinks
* free text markdown editing & display for descriptions
* formal change process and review (pull requests etc.)
* formal metadata structure for linking between use case elements
* validation of metadata structure / links.

## TODO:

* request specific help from Team Copper:
  * finish adding TOPmed user stories
  * KC6
  * get COPD in there/ask Team Carbon
  * add all the personas
  
  * ask Charles:
    * need a canonical URL that is long-lived; suggestions?
    * where should this be hosted? want versioning a la readthedocs, ~auto update.
    * note, hosting it on readthedocs is possible but need to commit the output/ directory!
    * can we put it in two places, one private (for private commenting etc.),
      the other public (with disqus and hypothesis also)?
    * (start by making it public.)

* add an explicit ordering option to the YAML header (lexicographic)
* add comments about where files are coming from
* add next, previous links.
* add use case glossary in as /glossary.md.
* add tagging to YAML header
* move repo under github.com/dcppc/.

## TODO medium term:
* link in idents in markdown descriptions, e.g. USERSTORY-5-foobar should be turned into a link to that user story.
* create an "errors" output page
* add spell checker
* add internal link checker
* add author/contact info to YAML header
