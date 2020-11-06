---
layout: default
title: Contributing
parent: Home
nav_order: 2
---

# Contributing to the NIH CFDE Use Case Library

Hello, and thank you for your interest in contributing to the CFDE Use Case Library!

By contributing to this repository, you agree:

1.  To obey the [Code of Conduct](./CODEOFCONDUCT.md)
2.  To release all your contributions under the same terms as the license itself: the [CC-BY Attribution 4.0 International](./LICENSE.md)

If you are OK with these two conditions, then we welcome both you and your contribution!

## How to develop a new use case

Each **use case** must include:

- a [**persona**](./glossary.md#persona)
- an [**objective**](./glossary.md#objective)
- a [**summary**](./glossary.md#summary) of the objective
- specific [**user tasks**](./glossary.md#user-task)
- technical infrastructure [**requirements**](./glossary.md#requirement) associated with user tasks

Start by drafting the components of your new use case idea and then read through the [use case library's](./full_list.md) existing persona, objective, user task, and requirement definitions. If any of them apply to your new use case, please reuse them! For example, multiple use cases may involve the persona "clinical researcher" (p-001) or the user task "access CFDE interface" (t-0001), so these *existing* files can be referenced in the new use case files and do *not* need to be recreated.

As necessary, you can also create new persona, objective, user task, or requirement files (see below for [file naming guidelines](#file-format-guide)). In particular, requirement files define the technical implementation for what needs to happen in user tasks. These may be difficult to define. You can include ideas for requirements with your use case submission and/or request help and we will reach out to the CFDE technical team for guidance.

Please see the [Use Case Style Guide](#usecasestyle) for format instructions!

## How to add content

If you have a suggestion for a new use case concept and are not familiar with GitHub, you can [email your idea to us](mailto:support@cfde.atlassian.net).

If you are familiar with GitHub please either:

  - Open a [`NewUseCase issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=new+use+case&template=NewUseCase_template.md&title=Add+use+case+idea+title) describing your new use case idea

  - Or write up your use case and submit it as a pull request (PR).

### PR process

If you are submitting a pull request, please create one pull request per new use case so admin can check the complete change. Please check that the new additions render correctly on the website before submitting the PR by rendering the website locally on your computer. You will need to make a [Github account](https://github.com/) and install [`git`](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git/) and [`conda`](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (e.g., by downloading Miniconda) on your computer. The instructions below have been tested on MacOS.

1\. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the [use case library repo](https://github.com/nih-cfde/use-case-library-build) and create a new branch in your forked version. For those onboarded to the CFDE, you may have permissions to edit the use case library repo directly instead of forking.

2\. Clone the repository to your local computer. Be sure to edit the command below with the correct Github user name:

```
git clone https://github.com/<your user name here>/use-case-library-test.git
cd use-case-library-build
```

3\. Create a conda environment to specify the software used to build the use case library website. The name of the environment is specified by the `-n` flag, for example "usecaselibrary". The `-f` flag specifies the file that has all the software requirements. This website stores those requirements in a file called "environment.yml". Once you have made the conda environment, you can skip to step 4 for future edits (assuming you don't delete this conda environment!).

```
conda env create -n usecaselibrary -f environment.yml
```

4\. Activate the conda environment.

```
conda activate usecaselibrary
```

5\. Now, either make a branch or switch to the branch you're making edits on if it already exists (e.g., if you created a branch on Github, you can switch to work on the remote branch).

```
# make branch
git branch <name of branch>

# switch to local branch
git checkout <name of branch>
```
```
# OR switch to remote branch
git checkout --track origin/<name of branch>
```

**New use case files should ONLY be added to the [`library` directory](https://github.com/nih-cfde/use-case-library-build/tree/latest/library). Please do not change any other files in the repository to prevent website rendering issues!**

Use the [use case file templates](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates) to format and add your new use case files to the `library` directory on your branch.

6\. After you've added the new use case files, preview how they look on the website! The website is built using snakemake rules. First, build the website's output directory. This should be done once. The `-j` flag specifies the number of cores to use; `-j 1` is sufficient for this website.

```
snakemake -j 1
```

7\. Generate the local render of the website. Scripts in this repository take the new files from the `library` directory, format them according to the website's stylesheets, and render them on the website.

```
snakemake serve -j 1
```

If this command executes successfully, copy the web address (`http://127.0.0.1:8000/`) to a web browser to check the changes you made. This is the local, offline version of the website! Note that if you continue to edit documents, you will need to use the `ctrl+c` keys on your keyboard to close the server, save changes, and re-run the `snakemake serve -j 1` command to view new changes.

Your terminal should show the following if the local render succeeds:
```
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Building documentation to directory: /var/folders/2k/dcjr_t3151z_s1yq8mlcv3f80000gn/T/mkdocs_alu91pc_
INFO    -  Documentation built in 0.35 seconds
INFO    -  Running at: http://127.0.0.1:8000/
INFO    -  Hold ctrl+c to quit.
```

8\. If you are satisfied with the changes, you can add, commit, and push the changes to your forked repo.

```
# add all new changes
git add .

# commit changes
git commit -am "short description of new changes"

# push changes
git push origin <name of branch>
```

If you are done working on the website, you can exit the conda environment to return to your base terminal environment.

```
conda deactivate
```

9\. After you push changes to your branch, you should see a message near the top of the Github repo page indicating that your branch is x number of commits ahead of `nih-cfde:latest`. There should be a button for "Pull request" and/or "Compare" - they lead to the same page to create a PR.
- Submit a PR pushing changes from your branch to `nih-cfde:latest`.
- Request reviews from Use Case maintainers by typing `@ACharbonneau` and `@marisalim` in your PR text box. Please check the to list in the PR text box (e.g., is the PR mergeable, etc.). You can continue to edit your PR after it has been submitted!
- Please allow up to one week for admin to review your request.

If you need help at any point in this process, please submit a [`HelpWanted issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=help+wanted&template=help_template.md&title=Add+problem+title)! Please include a reference (using `#`) to your PR number so we can check the submission.


### Use Case approval process

The Use Case committee will mark proposed use cases, and corresponding requirements pages, as `in progress`=&#x23F3;, `approved`=&#x1F44C;, and `done`=&#x2705;, as appropriate.

If you have any questions about contributing, please submit an issue and we will lend a hand as soon as possible:

Issue templates | About
--- | ---
[`NewUseCase issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=new+use+case&template=NewUseCase_template.md&title=Add+use+case+idea+title) | To describe and suggest a new use case idea
[`Enhancements issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=enhancement&template=Enhancement_template.md&title=Add+suggested+enhancement+title) | To suggest general improvements to the Use Case Library
[`HelpWanted issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=help+wanted&template=help_template.md&title=Add+problem+title) | To request general help
[`Bug report issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=bug&template=bug_template.md&title=Add+bug+title) | To report a bug

Thank you for being here and for being a part of the CFDE project!

## Use Case Library Style Guide <a name="usecasestyle"></a>

### General File Format Guidelines <a name="file-format-guide"></a>

**File names** should be lower case, use hyphens between words, and match the page titles (but try to keep them concise). All files should include a unique file ID. As indicated below, please add the appropriate number of leading 0's to the file IDs. The Use Case committee will finalize file IDs to ensure they do not clash with existing IDs.

   File type | File prefix | Example
   --- | --- | ---
   use case | uc-0000 | uc-0001-researcher-browse-and-filter.md
   persona | p-000 | p-001-clinical-researcher.md
   objective | obj-0000 | obj-0001-create-data-release.md
   user task | t-0000 | t-0001-access-cfde-interface.md
   requirement | r-00000 | r-00001-the-interface-will-support-gui-web-access-to-end-users.md

The **file format** for all files should be written in Markdown.

- For help with Markdown syntax, see this [basic syntax guide](https://www.markdownguide.org/basic-syntax/)
- To add links to other pages:
```
# syntax
[<text to click on>](<Github repo relative path to file>)

# This is an example for a link to the Personas description page for "Clinical Researcher":
[Clinical Researcher](./p-001-clinical-researcher.md)
```

The **site index** is automatically created by yaml headers at the top of each file. These headers will automatically render links to a use case's corresponding persona, objective, user task, and requirements files associated. The Use Case committee will check yaml headers to ensure the indices do not clash with existing files.

Yaml format begins and ends with "---". Every use case library page should have a `title:` key. For the [use case](#use-case-files) (uc-0000) and [user task](#user-task-files) (t-0000) files, additional keys and values are currently required. The additional keys (e.g., `requirements:`) are followed by a colon ":" and their corresponding values are listed after with a hyphen "-" and the file ID. Yaml keys may have one or more values. For example, the `requirements:` key below is linked to the `r-00003` and `r-00004` requirements file IDs:

```
---
title: example user task
requirements:
- r-00003
- r-00004
---
```

### Specific File Format Guidelines

#### `Use Case` files <a name="use-case-files"></a>
- Use the [use case file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-uc-template.md) to enter the required sections
- Each use case file submission must reference four types of file in the yaml header for the website to render properly:
    - 1 or more [persona files](#persona-files)
    - 1 or more [objective files](#obj-files)
    - 1 or more [user task files](#user-task-files)
    - 1 or more [requirement files](#req-files)
- Required sections:
    - yaml index header, including keys for `title:`, `persona:`, `objective:`, `user_tasks:`, and `requirements:`
    - a short summary of the use case

#### `Persona` files <a name="persona-files"></a>
- Use the [persona file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-persona-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:`
    - Short description of the persona's biological/computational experience, their role and responsibilities, and relation to any of the other personas in the Use Case Library
    - A bullet point section listing assumptions about the persona's credentials e.g., access to the CFDE

#### `Objective` files <a name="obj-files"></a>
- Use the [objective file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-obj-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:`
    - a brief ~1-2 sentence description of the objective

#### `User task` files <a name="user-task-files"></a>
- Use the [user task file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-task-template.md) to enter the required sections
- The User Tasks title should be short and self-explanatory. You can add a short description in the main text (not yaml header) as needed for clarity.
- Each user task must reference 1 or more requirements in the yaml header for the website to render properly
- Required sections:
    - yaml index header with `title:` and `requirements:`

#### `Requirement` files <a name="req-files"></a>
- Use the [requirement file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-reqs-template.md) to enter the required sections
- The Requirements title should be short and self-explanatory. You can add a short description in the main text (not yaml header) as needed for clarity.
- Required sections:
    - yaml index header with `title:`
