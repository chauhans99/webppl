# MIT 6.804 Final Project 


## Overview

For our 6.804 final project, we created 2 different types of Bayesian models (expert-derived and data-derived) and evaluated their respective accuracies in predicting diabetes in a dataset of Pima Indians.

We used data from https://kaggle.com/kumargh/pimaindiansdiabetescsv, which is stored as pima-indians-diabetes.csv in our repo, to train and evaluate our models.

We ran the expert-derived Bayesian model 3 ways (expert_derived_complete_data.wppl, expert_derived_incomplete_data.wppl, expert_derived_subset_data.wppl) and the data-derived Bayesian model 3 ways (data_derived_complete_data.wppl, data_derived_incomplete_data.wppl, data_derived_subset_data.wppl).
* complete_data refers to the entire dataset, unpruned
* incomplete_data refers to the dataset pruned to take out missing or incomplete data points
* subset_data refers to the dataset pruned to take out pregnant women

## Methodology

* Install webppl (https://webppl.readthedocs.io/en/master/installation.html) so you can run .wppl files.
* Data pruning: run `python parseData.py` with the following modification (if applicable): 
  * Use `if True:` instead of line 18 to get complete_data. 
  * Use ` not row[2] == '0' and not row[3] == '0' and not row[5] == '0' ` instead of line 18 to get incomplete_data. 
  * Keep line 18 to get subset_data
* Paste the data into the Bayesian models: You will get 3 lists logged in the terminal as a result of running parseData.py.
  * Enclose the first list in quotes to create a string object and assign `var observedData` in data_derived_complete_data.wppl, data_derived_incomplete_data.wppl, data_derived_subset_data.wppl to the string.
  * Enclose the second list in quotes to create a string object and assign `var testData` in all 6 .wppl files (expert_derived_complete_data.wppl, expert_derived_incomplete_data.wppl, expert_derived_subset_data.wppl, data_derived_complete_data.wppl, data_derived_incomplete_data.wppl, data_derived_subset_data.wppl)  in the repo to the string.
  * Assign `var answer` in all 6 .wppl files (expert_derived_complete_data.wppl, expert_derived_incomplete_data.wppl, expert_derived_subset_data.wppl, data_derived_complete_data.wppl, data_derived_incomplete_data.wppl, data_derived_subset_data.wppl)to the 3rd list.
* Run the Bayesian models with by running something like `webppl expert_derived_complete_data.wppl` in the terminal
* Look at the results logged in the terminal.
   * in expert-derived models: The logged list contains 20 integers. Each integer corresponds to one of the test data points used to evaluate the model. 1 means that the model correctly predicted if the subject had diabetes, while 0 means that the model was incorrect. The accuracy of the model on the test data points is printed below the list.
   * in data-derived models: the link parameters that the model returns after learning from the data is logged. Underneath, it prints out if the model returns 1 or 0 for each data point. Finally, the accuracy of the model on the test data points is printed at the bottom.

