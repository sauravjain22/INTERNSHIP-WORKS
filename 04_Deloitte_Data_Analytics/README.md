# Deloitte Australia – Data Analytics Job Simulation

## Overview

This project was completed as part of the **Deloitte Australia Data Analytics Job Simulation on Forage**.

The simulation provided practical experience working with business data and applying data analytics and forensic technology techniques to investigate real-world style business problems.

The project consisted of two tasks:

1. Data Analysis
2. Forensic Technology

---

## Task 1 – Data Analysis

### Objective

The objective was to analyse telemetry data collected by **Daikibo Industrials** using **Tableau**.

The analysis focused on identifying machine downtime across factories and device types.

### Work Performed

- Imported Daikibo telemetry data into Tableau
- Created a calculated measure called `Unhealthy`
- Assigned 10 minutes of potential downtime to each unhealthy status
- Created a **Down Time per Factory** bar chart
- Created a **Down Time per Device Type** bar chart
- Built an interactive dashboard
- Configured the factory chart to act as a filter
- Identified the factory with the highest downtime
- Analysed device downtime for the selected factory

### Key Finding

The factory with the highest downtime was:

**Daikibo Factory Seiko**

The dashboard was then filtered to this factory to investigate downtime by device type.

### Tool Used

- Microsoft Tableau

---

## Task 2 – Forensic Technology

### Objective

Daikibo Industrials wanted to investigate concerns regarding **gender inequality in salary**.

An Equality Table containing factory, job role and equality score information was provided.

### Dataset

The original table contained:

- Factory
- Job Role
- Equality Score

The equality score ranges from **-100 to +100**, with **0 representing ideal equality**.

### Work Performed

A fourth column called:

```text
Equality class