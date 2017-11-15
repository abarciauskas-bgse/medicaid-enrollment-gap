# create a linear model for poverty levels for each state
# something like percent_of_fpl * x = percent_of_population
# What is X?
from sklearn import linear_model
import csv
import numpy as np

# max of each level, ignoring the last column 400+ which gives no new information
levels = np.array([100, 199, 399]).reshape(-1, 1)
levels_to_predict = np.array([138]).reshape(-1, 1)

predictions = []
# Data from https://www.kff.org/other/state-indicator/distribution-by-fpl
# Downloaded CSV and deleted top line
with open('data/raw_data.csv') as csvfile:
  filereader = csv.reader(csvfile)
  next(filereader, None)  # skip the headers
  for row in filereader:
    state = row[0]
    percent_in_level = list(map(float, row[1:4]))
    percent_in_level = np.array(percent_in_level).reshape(-1, 1)
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(levels, percent_in_level)
    # Make predictions using the testing set
    levels_prediction = regr.predict(levels_to_predict)
    predictions.append([state, round(levels_prediction[0][0]*100, 2)])

with open("data/interpolation_output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(predictions)
