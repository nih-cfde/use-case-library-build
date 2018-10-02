# Use Case Library

## Getting started

(You'll need to install the packages in `requirements.txt`.)

Run:

```
snakemake
```

and then open `output/site/index.html`.

You can see a deployed version at <http://nih-data-commons.us/use-case-library>.

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
* (Optional) Build the file using `snakemake`, check the output. Iterate until you're happy.
* Add new file to git repo, commit, push.
* Set up a Pull Request to merge into master and tag in @ctb.
* [Uncle Arche](https://github.com/dcppc/uncle-archie) will check out a copy of 
  your pull request and run `snakemake build` on it, and link to the output of
  the build process, so you can use Uncle Archie instead of using snakemake locally

## Higher order goals / why we did this:

* stable URL structure and permalinks
* free text markdown editing & display for descriptions
* formal change process and review (pull requests etc.)
* formal metadata structure for linking between use case elements
* validation of metadata structure / links.

## TODO medium term:

* add comments about where files are coming from
* link in idents in markdown descriptions, e.g. USERSTORY-5-foobar should be turned into a link to that user story.
* create an "errors" output page
* add spell checker
* add internal link checker
* add author/contact info to YAML header

