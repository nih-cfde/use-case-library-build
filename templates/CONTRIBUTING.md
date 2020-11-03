---
layout: default
title: Contributing
parent: Home
nav_order: 2
---

# Contributing to the nih-cfde Use Case Repository

Hello, and thank you for your interest in contributing to the CFDE Use Case Repository!

By contributing to this repository, you agree:

1.  To obey the [Code of Conduct](./CODEOFCONDUCT.md)
2.  To release all your contributions under the same terms as the license itself: the [CC-BY Attribution 4.0 International](./LICENSE.md)

If you are OK with these two conditions, then we welcome both you and your contribution!

## How to add content

If you have a suggestion for a new use case concept and are not familiar with GitHub, you can [email your idea to us](mailto:support@cfde.atlassian.net).

If you are familiar with GitHub please either:

  - Open a [`NewUseCase issue`](https://github.com/nih-cfde/use-case-library-build/issues/new?labels=new+use+case&template=NewUseCase_template.md&title=Add+use+case+idea+title) describing your new use case idea

  - Or write up your use case and submit it as a pull request (PR). Please follow the [Use Case Style Guide](#usecasestyle) below.

### PR process
If you are submitting a pull request, please create one pull request per use case so admin can check the complete change.

  - [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the [use case library repo](https://github.com/nih-cfde/use-case-library-build) and create a new branch in your forked version.

  **New use case files should ONLY be added to the [`library` directory](https://github.com/nih-cfde/use-case-library-build/tree/latest/library). Please do not change any other files in the repository!**

  - Use the [use case file templates](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates) to format and add your new use case files to the `library` directory on your branch.
  - After you add changes to your branch, you should see a message near the top of the repo page indicating that your branch is x number of commits ahead of `nih-cfde:latest`. There should be a button for "Pull request" and/or "Compare" - they lead to the same page to create a PR. Submit a PR pushing changes from your branch to `nih-cfde:latest`.
  - Request reviews from Use Case maintainers by typing `@ACharbonneau` and `@marisalim` in your PR text box
  - Please allow up to one week for admin to review your request

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

## Use Case Repository Style Guide <a name="usecasestyle"></a>

### Use Case Structure
- All Use Cases must have:
    - a **Persona**
    - an **Objective**
    - a **Summary** of the Objective
    - specific **User Tasks**
    - technical infrastructure **Requirements** for each User Task
- See [glossary](./glossary.md) for definitions
- Each persona, objective, user task, and requirement needs its own description page that will be linked to the corresponding use case page(s). Common user tasks and requirements should be reused across use cases.

### General File Format Guidelines

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

The **site index** is automatically created by yaml headers at the top of each file. These headers will automatically render links to the corresponding persona, objective, user task, and requirements files associated with a given use case. The Use Case committee will check yaml headers to ensure the indices do not clash with existing files.

Yaml format begins and ends with "---". Every use case library page should have a `title:` key. For the [use case](#use-case-files) (uc-0000) and [user task](#user-task-files) (t-0000) files, additional keys and values are currently required. The additional keys (e.g., `requirements:`) are followed by a colon ":" and their corresponding values are listed after with a hyphen "-" and the file ID. Yaml keys may have one or more values. For example, the `requirements:` key below is linked to the `r-00003` and `r-00004` requirements file IDs:

```
---
title: example user task
requirements:
- r-00003
- r-00004
---
```

### `Use Case` files <a name="use-case-files"></a>
- Use the [use case file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-uc-template.md) to enter the required sections
- Required sections:
    - yaml index header, including keys for `title:`, `persona:`, `objective:`, `user_tasks:`, and `requirements:`
    - a short summary of the use case

### `Persona` files
- Use the [persona file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-persona-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:`
    - Short description of the persona's biological/computational experience, their role and responsibilities, and relation to any of the other personas in the Use Case Library
    - A bullet point section listing assumptions about the persona's credentials e.g., access to the CFDE

### `Objective` files
- Use the [objective file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-obj-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:`
    - a brief ~1-2 sentence description of the objective

### `User task` files <a name="user-task-files"></a>
- The User Tasks title should be short and self-explanatory, but please add a short description as needed for clarity
- Use the [user task file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-task-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:` and `requirements:`

### `Requirement` files
- The Requirements title should be short and self-explanatory, but please add a short description as needed for clarity
- Use the [requirement file template](https://github.com/nih-cfde/use-case-library-build/tree/latest/library_file_templates/library-reqs-template.md) to enter the required sections
- Required sections:
    - yaml index header with `title:`
