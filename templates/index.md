---
layout: default
title: Home
nav_order: 1
has_children: true
---

# Use Case Library

The Use Case Library provides a set of high-level summaries that capture the essential scientific objectives
and place them in the context of larger goals and the Common Fund Data Ecosystem timeline.

You can explore the library using the tabs above.

We welcome new contributions.
Please read the [contributor guidelines](./about/contributing.md) before submitting a pull request.


## Overview

A **Use Case** consists of an **Objective** and a **Persona** -
a person who can have an **Objective**. These are combined into a **summary**
of specific use for the CFDE, which can be achieved by a series
of **user tasks**. Each **User Task** is single step in the users workflow.
The technical infrastucture required
to enable a **User Task** are it's **Requirements**. In most cases, what
appears to the user as a single step actually is a multistep process to the
computer doing the work, so any given **User Task** will likely have many **Requirements**.
Both **user tasks** and **requirements** can be shared across **Use Cases**


![Use case library glossary image](./images/UseCaseTopDown.jpg)

## Full Listing of Library Entries

View the comprehensive list of library entries [here](full_list.md).

The Use Case Library contains {{ len(yield_objects('USE CASE')) }} use
cases, {{ len(yield_objects('OBJECTIVE')) }} objectives,
{{ len(yield_objects('TASK')) }} tasks, and
{{ len(yield_objects('REQUIREMENT')) }} requirements, for
{{ len(yield_objects('PERSONA')) }} personas.
