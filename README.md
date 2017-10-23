# Which states are underenrolled in Medicaid?

One of the things we've started working on at Nava is [integrated benefits](https://www.navapbc.com/work/benefits-partnership/). Integrated benefits is the idea that any given individual or household may be eligible for one or more social services programs and in order to enroll in those programs, they shouldn't need to provide the same information multiple times.

Many of the social services are administered at the state level. How do we prioritize where to develop integrated services?

One simplistic approach I'm trying is to see where there is the greatest need - where are there many people who are missing out on these services?

Using Medicaid, poverty and population data from census.gov and medicaid.gov, we can estimate a "Medicaid enrollment gap". One thing I was surprised to find was most states are actually "over-enrolled": more individuals are enrolled in Medicaid than are living under the poverty line. However, this shouldn't have been surprising. Each state is given freedom to enforce it's own eligibility rules.

The [ACA enforced one rule uniformly](https://en.wikipedia.org/wiki/Medicaid): everyone with income below 133% of the poverty line is eligible for Medicaid. However this provision of the ACA was overruled in the Supreme Court:

> However, the Supreme Court ruled in NFIB v. Sebelius that this provision of the ACA was coercive, and that the federal government must allow states to continue at pre-ACA levels of funding and eligibility if they chose.

So while most states have more Medicaid enrollees than population living under the poverty line, a few states do not and their gaps really appear as outliers in the data. And you can really see that those states with smaller or negative gaps between Medicaid enrollees and population in poverty correspond to those states who have chosen  not to expand Medicaid under the ACA.

# Data

* Poverty data from census.gov
  * [page](https://www.census.gov/data/tables/2017/demo/income-poverty/p60-259.html)
  * [xls file](https://www2.census.gov/programs-surveys/demo/tables/p60/259/statepov.xls)
* Population data from census.gov
  * [page](https://www2.census.gov/programs-surveys/popest/datasets/2010-2016/state/asrh/)
  * [csv file](https://www2.census.gov/programs-surveys/popest/datasets/2010-2016/state/asrh/scprc-est2016-18+pop-res.csv)
* Medicaid enrollment from medicaid.gov
  * [page](https://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-enrollment-data/enrollment-mbes/index.html)
  * [pdf file](https://www.medicaid.gov/medicaid/program-information/downloads/cms-64-enrollment-report-jul-aug-2016.pdf) - copy / pasted data to create CSV
  * data not available for South Dakota
