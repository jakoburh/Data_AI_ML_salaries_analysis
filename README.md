# Data, AI & ML Salaries Analysis (2020–2025)

Exploratory analysis of salaries and working arrangements in data, artificial intelligence and machine-learning roles using Excel, Python and Streamlit.

This was one of my early projects while learning Python for data analysis. I deliberately analysed the same dataset in **Microsoft Excel and Python**, attempting to reproduce the same calculations with both tools.

The goal was not only to investigate salary patterns, but also to understand how spreadsheet-based analysis translates into programming concepts such as filtering, grouping, dictionaries, loops, functions and DataFrames.

I have kept the original 2025 Python code in this repository, including some inefficient and experimental approaches. It reflects how I was learning at the time rather than how I would structure the same project today.

## Questions

I focused on several questions:

- How many different job titles are represented in the dataset?
- Which roles appear most frequently?
- How do average salaries differ between jobs?
- How does experience level affect salary?
- Which job titles have the highest median salaries?
- How reliable are salary estimates for rare job titles?
- How common is remote work across different roles?
- Is remote work associated with noticeably different salaries?
- Can I reproduce the same analysis independently in Excel and Python?

## Dataset

The dataset contains salary observations from **2020 to 2025** for jobs related to data science, artificial intelligence, machine learning and related technical fields.

Variables used in the analysis included:

- work year
- experience level
- employment type
- job title
- salary
- salary currency
- salary in USD
- employee residence
- remote-work ratio
- company location
- company size

The dataset contained **398 unique job titles**, ranging from common roles such as Data Scientist, Data Engineer and Data Analyst to highly specialized titles that appeared only a few times.

Because many titles described similar types of work, I also manually grouped jobs into broader categories for part of the analysis.

## Tools

### Microsoft Excel

The Excel analysis used:

- pivot tables
- `XLOOKUP`
- `AVERAGEIFS`
- `COUNTIFS`
- `UNIQUE`
- `FILTER`
- `MEDIAN`
- conditional formatting
- manual job-title grouping
- charts and summary tables

### Python

The Python analysis used:

- Python
- Pandas
- NumPy
- Matplotlib
- dictionaries
- nested dictionaries
- loops and conditional logic
- custom functions
- DataFrames and pivot-style tables

### Dashboard

I later built an interactive dashboard using:

- Streamlit
- Pandas
- Altair

The dashboard allows users to explore salaries by job title, grouped title and experience level and displays average salaries, median salaries, remote-work information and sample sizes.

## Learning approach: Excel vs Python

A major purpose of this project was to answer the same questions using two different approaches.

For example:

| Task | Excel | Python |
| --- | --- | --- |
| Count unique job titles | Pivot tables / formulas | `nunique()` |
| Calculate average salaries | Pivot tables | `groupby().mean()` |
| Convert currencies | `XLOOKUP` | dictionary + `.map()` |
| Group job titles | lookup table | mapping dictionary |
| Calculate medians | `FILTER` + `MEDIAN` | custom function / Python logic |
| Compare experience levels | pivot tables | dictionaries / DataFrames |
| Analyse remote work | pivot tables + `COUNTIFS` | loops, dictionaries and functions |
| Visualize results | Excel charts | Matplotlib / Altair |

At the time, I intentionally tried to recreate calculations manually in Python rather than relying only on convenient Pandas functions.

This sometimes resulted in unnecessarily complicated code, but it helped me understand what operations such as grouping, counting, averaging and filtering actually do underneath higher-level library functions.

## Data preparation

### Currency conversion

The dataset contained salaries in multiple currencies.

For the project, I created a fixed currency-conversion table and converted salaries into euros so that salaries could be compared using the same unit.

In Excel, I used `XLOOKUP` to match each currency with its conversion coefficient.

In Python, I created a dictionary of currency codes and conversion rates and used Pandas `.map()` before calculating:

`salary in EUR = salary × conversion rate`

This conversion was intended to make values comparable within the project rather than reconstruct historically accurate exchange rates for every salary year.

### Grouping job titles

The dataset contained **398 different job titles**, making many visual comparisons impractical.

I manually grouped similar jobs into broader categories such as:

- AI
- Data
- Analyst
- Programming
- Research
- Business
- Manager
- Bioinformatics
- Statistician

The same grouping logic was recreated in both Excel and Python.

This grouping was subjective and represents my interpretation of related roles rather than an established industry taxonomy.

## Analysis

### Job-title diversity

The dataset contained **398 unique titles**.

Some roles appeared thousands of times, while many highly specialized titles appeared only once or a handful of times.

**Data Scientist** was the most frequent individual title in the dataset.

This immediately demonstrated an important statistical problem: salary estimates for common jobs are supported by much larger samples than estimates for rare jobs.

### Salary and experience level

I compared salaries across four experience categories:

- **EN** — Entry level
- **MI** — Mid-level
- **SE** — Senior
- **EX** — Executive

Across many comparable roles, salaries generally increased with experience.

The pattern was not perfectly consistent for every grouped category because salaries were also affected by factors such as:

- job-title grouping
- location
- company characteristics
- sample size
- extreme values
- year of observation

The main result was therefore not that every senior worker earns more than every junior worker, but that higher experience levels were generally associated with higher salaries across the dataset.

## Average vs median salary

I calculated both average and median salaries.

This became important because some job titles had very small sample sizes.

A rare title represented by only one or two highly paid workers can produce an extremely high average or median salary even though the value tells us very little about the wider labour market.

Median salaries therefore needed to be interpreted together with the number of observations behind them.

This was one of the first projects where I became aware that a technically correct statistic can still be misleading if the sample behind it is too small.

## Remote work

The dataset coded work arrangements using:

- `0` — office-based
- `50` — hybrid
- `100` — fully remote

I compared the prevalence of these categories between job groups and examined salaries across remote and office-based work.

Remote work was common across many data-related roles, while hybrid observations were relatively uncommon in this dataset.

I did not observe a large or consistent salary difference attributable purely to remote status within comparable roles.

However, this analysis does not control for other factors such as country, experience, company size or job specialization, so it should not be interpreted as evidence that remote work has no effect on salary.

## Streamlit dashboard

After completing the main analysis, I created a Streamlit dashboard to make the dataset easier to explore interactively.

Users can select:

- experience level
- individual job title
- grouped job category

The dashboard can display:

- average salary
- median salary
- percentage of remote work
- average salary among remote observations
- number of observations supporting the calculation

I also added visualizations comparing average salaries, median salaries and remote-work prevalence between grouped job categories.

A custom graph section allows different dimensions of the dataset to be explored interactively.

## Main findings

Based on this dataset:

- the dataset contained **398 unique job titles**;
- a relatively small number of common roles accounted for a large proportion of observations;
- salaries generally increased with experience level;
- some of the highest median salaries belonged to rare job titles with very small samples;
- common roles produced more stable salary estimates because they contained substantially more observations;
- remote work was common in data-related professions;
- I did not observe a major salary difference between remote and office-based work within comparable roles;
- analysing the same questions in Excel and Python generally produced similar results and helped me identify errors and differences in implementation.

## Limitations

The project has several important limitations.

### Uneven sample sizes

Job titles were represented very unevenly.

Some roles contained thousands of observations while others appeared only once. Very high average or median salaries for rare titles should therefore be interpreted cautiously.

### Subjective job grouping

The grouping of 398 individual job titles into broader categories was performed manually.

Some titles could reasonably belong to several different groups, meaning that another analyst could create a different classification and obtain somewhat different group-level results.

### Currency conversion

I converted salaries using a fixed set of exchange rates for the project.

Exchange rates change over time, and the analysis does not reconstruct the historical exchange rate applicable to every salary observation.

### Inflation

Salaries from 2020 and 2025 were compared without adjustment for inflation.

A nominal salary from 2020 is therefore not directly equivalent in purchasing power to the same nominal salary in 2025.

### Other salary determinants

The analysis did not fully control for:

- country and cost of living
- working hours
- employee benefits
- company size
- industry
- education
- job responsibilities

These factors may explain some of the salary differences attributed to job title, experience or remote work.

### Early Python implementation

The Python code in this repository represents my skill level while I was learning.

Some operations that could now be performed with concise Pandas methods were instead implemented manually using loops, nested dictionaries and custom functions.

There are also experimental and abandoned approaches preserved in the code.

For that reason, the repository should be viewed as both a data-analysis project and a record of my learning process rather than as production-ready software.

### Dashboard portability

The original Streamlit dashboard reads data from locally defined file paths and from preprocessed sheets in the Excel workbook.

It therefore requires modification before it can be deployed as a fully portable application.

## What I learned

This project was particularly important for learning how programming relates to spreadsheet analysis.

It taught me how to:

- translate Excel operations into Python;
- work with Pandas DataFrames;
- group and aggregate large datasets;
- use dictionaries and nested data structures;
- write custom functions;
- calculate averages and medians programmatically;
- understand how sample size affects interpretation;
- distinguish between mean and median;
- create charts using Matplotlib;
- build an interactive dashboard with Streamlit;
- use Altair for interactive visualization;
- debug differences between two independent implementations of the same calculation;
- recognize when my own solution is unnecessarily complicated;
- preserve failed approaches as part of learning rather than hiding them.

One example was an early attempt to encode both salary totals and observation counts using mathematical operations with prime numbers.

The approach quickly became impractical for a large dataset, so I replaced it with a much simpler structure storing the salary sum and counter separately.

Although the original idea was inefficient, working through why it failed helped me understand data structures and aggregation more deeply.

Looking back at the project now, I would solve many of these problems much more simply using Pandas operations such as `groupby`, `agg`, `median` and reusable data-processing functions.

That difference between the original code and how I would approach the problem today is one of the main reasons I have kept the 2025 version.

## Repository contents

- `salaries_analysis_2025.xlsx` — original Excel analysis, calculations, pivot tables and processed data
- `code_2025.py` — original Python analysis and learning code
- `dashboard_2025.py` — original Streamlit dashboard
- `salaries_report.pdf` — written report describing the analysis, methodology and original interpretation

## Possible future improvements

If I revisited this project, I would:

- preserve the original 2025 version as a record of my learning;
- rebuild the analysis from the raw dataset using a reproducible Pandas pipeline;
- separate data cleaning, analysis and visualization into reusable functions;
- replace manual loops and nested dictionaries where vectorized Pandas operations are more appropriate;
- remove hard-coded local file paths;
- load the dashboard directly from processed data generated by the Python pipeline;
- use a documented and reproducible job-title classification system;
- adjust salaries for inflation;
- handle historical currency conversion more carefully;
- formally compare salary differences while controlling for experience, location and other variables;
- add automated checks to confirm that Excel and Python results match;
- make the Streamlit dashboard deployable online;
- compare the refactored results with the original 2025 analysis and document what changed.

The original version is intentionally preserved because the project is not only about salary data. It also documents how my approach to programming and data analysis developed over time.
