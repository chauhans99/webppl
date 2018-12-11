import csv
import random

def parseData(result, num_data):

	with open('pima-indians-diabetes.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
		# total_rows_used = 0
		# age_35_to_49 = 0
		# age_over_50 = 0
		# overweight_bmi = 0
		# obese_bmi = 0
		# high_blood_pressure = 0
	    # row format is each person's data([preganancies, glucose, blood pressure, skin thickness, insulin, bmi, diabetes pedigree, age, class])
	    for row in csv_reader:
			#also now not using row where the value is 0, meaning no actual value was recorded

	    	if row[0] == '0' and not row[2] == '0' and not row[3] == '0' and not row[5] == '0': # only considering not pregnant women (so we don't need to worry about extraneous effect of gestational diabetes)
	    		patient = {}

	    		age = int(row[7])
	    		if (age >= 35 and age <= 49):
	    			patient["observed_age_35_to_49"] = 1
	    			patient["observed_age_over_50"] = 0
	    		elif (age >= 50):
	    			patient["observed_age_35_to_49"] = 1
	    			patient["observed_age_over_50"] = 0
	    		else:
	    			patient["observed_age_35_to_49"] = 0
	    			patient["observed_age_over_50"] = 0

	    		bmi = float(row[5])
	    		if (bmi >= 25 and bmi <=29.9):
	    			patient["observed_overweight_BMI"] = 1
	    			patient["observed_obese_BMI"] = 0
	    		elif (bmi >29.9):
	    			patient["observed_overweight_BMI"] = 0
	    			patient["observed_obese_BMI"] = 1
	    		else:
	    			patient["observed_overweight_BMI"] = 0
	    			patient["observed_obese_BMI"] = 0

	    		blood_pressure = float(row[2])
	    		if (blood_pressure >= 80):
	    			patient["observed_high_blood_pressure"] = 1
	    		else:
	    			patient["observed_high_blood_pressure"] = 0

	    		diabetes = int(row[8])
	    		patient["observed_diabetes"] = diabetes

	    		skin_thickness = int(row[3])
	    		if (skin_thickness >= 30):
	    			patient["observed_skin_thickness"] = 1
	    		else:
	    			patient["observed_skin_thickness"] = 0


	    		if (num_data > 0):
	    			result.append(patient)
	    			num_data -= 1

	    return result

def transform_to_string(temp):
	temp = str(temp)
	newstring = ""
	for char in temp:
		if (char == '\''):
			newstring += '\"'
		else:
			newstring += char
	return newstring

result = []
num_data = 700 # how many data points you want to put in your observedData list 
num_test_data = 20
temp = parseData(result, num_data)

actual = [i for i in range(len(temp))]
choices = random.sample(actual, num_test_data)

final_result, final_test, patient_data = [], [], []
for i, v in enumerate(result):
	if i in choices:
		patient_data.append(v['observed_diabetes'])
		del v['observed_diabetes']
		final_test.append(v)
	else:
		final_result.append(v)

print(len(final_result))
print(transform_to_string(final_result))
print(transform_to_string(final_test))
print(patient_data)

# this is super jank, but basically copy what is printed in the console when you run python parseData.py
# and then paste it as ___ in var observedData = ___ (which is in model_v1.wppl)
