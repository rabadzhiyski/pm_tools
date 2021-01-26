# Project Management Metrics - pm_tools
The tool calculates the most popular metrics in traditional/predictive project management (aka "Waterfall"). All you need to do is to run it and after that call "Metrics()" with the respective inputs: **planned percent complete (float), budget (int), actual percent complete (float), actual cost (int).** 

## Contents
The repository contains the installation package and a jupyter file for those who want to avoid "pip install".

## Installation

pip install pm-tools

## How to use it the tool

1. **Import the libraries**

from pm_tools import Metrics

2. **Create a variable with the respective inputs** (planned percent complete, budget, actual percent complete, actual cost), **the input order is important!**

milestone_1 = Metrics(0.5, 100000, 0.4, 20000)

3. **Call the available metrics:**
- milestone_1.planned_value()
- milestone_1.earned_value()
- milestone_1.schedule_variance()
- milestone_1.cost_variance()
- milestone_1.schedule_perf_index()
- milestone_1.cost_perf_index()

## A few hints how to read the metrics/results:

- **Planned Value** - a measure of the estimated cost of planned activities at any given time.
- **Earned Value** - gives the actual value. It is based on the work already done, not the work you should have done in the project. Comparing Earned Value with Planned Value gives a quick estimate of whether you’re behind or ahead of schedule.
- **Actual Cost** - a measure of the actual expenses incurred in completing all of the work done to date. Actual Cost gives a broad understanding of project expenses.
- **Schedule Variance** - tells if the project is ahead or behind schedule. If SV > 0, it means that more value than planned is earned (ahead of schedule). If SV < 0, it means the project is behind schedule, and if it is 0, it means that project is on time.
- **Cost Variance** - tells whether the project is on budget(CV = 0), over (CV < 0), or under-budget (CV > 0).
- **Schedule Performance Index** - related to Schedule Variance. Whether the project is following its schedule but expressed as a ratio, not as an absolute figure. SPI > 1 (ahead of scheudle), SPI < 1 (behind schedule), SPI = 1 (on time).
- **Cost Performance Index** - related to Cost Variance. Whether the project is on budget but expressed as a ratio, not as an absolute figure. CPI > 1 (under budget), CPI < 1 (over budget), CPI = 1 (on budget).

## Acknowledgements
- The creation of the metrics was based on [PMI's approach](https://pmi.org) 
- It covers only basic project management metrics, that in general show project performance
- It's Project Manager's job to track project's health

