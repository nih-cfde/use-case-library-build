---
layout: default
title: Home
nav_order: 1
has_children: true
---

# Use Case Library

The Use Case Library provides a set of high-level summaries that captures essential scientific objectives
and places them in the context of larger goals in the Common Fund Data Ecosystem timeline.

You can explore the library using the tabs above.

We welcome new contributions.
Please read the [contributor guidelines](CONTRIBUTING.md) before submitting a new use case.



## Overview

A **Use Case** consists of an **Objective** and a **Persona** -
a person who can have an **Objective**. These are combined into a **summary**
of specific use cases for the CFDE, which can be achieved by a series
of **user tasks**. Each **User Task** is a single step in the user's workflow.
The technical infrastructure required
to enable a **User Task** are its **Requirements**. In most cases, what
appears to the user as a single step actually is a multi-step process to the
computer doing the work, so any given **User Task** will likely have many **Requirements**.
Both **user tasks** and **requirements** can be shared across **Use Cases**.

![Use case library glossary image](./images/UseCaseTopDown.jpg)

## Full Listing of Library Entries

View the comprehensive list of library entries [here](full_list.md).

The Use Case Library contains {{ len(yield_objects('USE CASE')) }} use
cases, {{ len(yield_objects('OBJECTIVE')) }} objectives,
{{ len(yield_objects('TASK')) }} tasks, and
{{ len(yield_objects('REQUIREMENT')) }} requirements, for
{{ len(yield_objects('PERSONA')) }} personas.
