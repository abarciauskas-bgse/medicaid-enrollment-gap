import csv
import pandas as pd

population_metadata = {
 'file': 'data/scprc-est2016-18+pop-res.csv',
 'state_col': 'NAME',
 'data_col': 'POPESTIMATE2016'
}

medicaid_metadata = {
  'file': 'data/cms-64-enrollment-report-jul-aug-2016.csv',
  'state_col': 'State',
  'data_col': 'Total Medicaid Enrollees'
}

poverty_metadata = {
  'file': 'data/interpolation_output.csv',
  'state_col': 'State',
  'data_col': 'poverty_perct'
}

# TODO(aimee): Create function for all this
with open(population_metadata['file']) as f:
  population = pd.DataFrame([{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)])
  data_col = population_metadata['data_col']
  population[data_col] = [int(value.replace(',','')) for value in population[data_col]]

with open(medicaid_metadata['file']) as f:
  medicaid_enrollment = pd.DataFrame([{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)])
  data_col = medicaid_metadata['data_col']
  medicaid_enrollment[data_col] = [int(value.replace(',','')) for value in medicaid_enrollment[data_col]]

with open(poverty_metadata['file']) as f:
  poverty_rates = pd.DataFrame([{k: v for k, v in row.items()} for row in csv.DictReader(f, skipinitialspace=True)])
  data_col = poverty_metadata['data_col']
  poverty_rates[data_col] = [float(value.replace(',','')) for value in poverty_rates[data_col]]  

merged_data = population.merge(
  medicaid_enrollment,
  left_on=population_metadata['state_col'],
  right_on=medicaid_metadata['state_col'])

merged_data = merged_data.merge(
  poverty_rates,
  left_on=population_metadata['state_col'],
  right_on=poverty_metadata['state_col'])

# Medicaid expansion covers all those earning 133% of the poverty level, but
# there's no good way to factor this in w/o knowing the distribution of income
# levels.
# https://www.healthcare.gov/medicaid-chip/medicaid-expansion-and-you/
merged_data['medicaid_rate'] = (merged_data[medicaid_metadata['data_col']] / merged_data[population_metadata['data_col']]) * 100
merged_data['gap'] = (merged_data['medicaid_rate'] - merged_data['poverty_perct']).round(2)

print(merged_data[['NAME','medicaid_rate','poverty_perct','gap']])
pd.DataFrame.to_csv(merged_data[['NAME','medicaid_rate','poverty_perct','gap']], path_or_buf='medicaid-poverty-gap.csv')


