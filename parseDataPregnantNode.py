import csv
import random

def parseData(result, num_data):

	with open('pima-indians-diabetes.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
            age_35_to_49 = 0.0
            age_over_50 = 0.0
            overweight_BMI = 0.0
            obese_BMI  = 0.0
            high_blood_pressure = 0.0
	    pregnant = 0.0
	    # row format is each person's data([preganancies, glucose, blood pressure, skin thickness, insulin, bmi, diabetes pedigree, age, class])
	    for row in csv_reader:
	    	# row[0] = pregnancy, row[2] = blood pressure, row[3] = blood pressure, row[5] = bmi
	    	# if row[_] = '0', then r[_] has no data for the field (ie row[0] == '0' means that the woman has never been pregnant)

	    	if not row[2] == '0' and not row[3] == '0' and not row[5] == '0': # only considering not pregnant women (so we don't need to worry about extraneous effect of gestational diabetes)
	    		patient = {}
			pregnancy = int(row[0])
			if pregnancy >= 11:
                                pregnant += 1
				patient["observed_pregnancy"] = 1
			else:
                                patient["observed_pregnancy"] = 0

	    		age = int(row[7])
	    		if (age >= 35 and age <= 49):
	    			patient["observed_age_35_to_49"] = 1
	    			patient["observed_age_over_50"] = 0
	    			age_35_to_49 += 1
	    		elif (age >= 50):
	    			patient["observed_age_35_to_49"] = 1
	    			patient["observed_age_over_50"] = 0
	    			age_over_50 += 1
	    		else:
	    			patient["observed_age_35_to_49"] = 0
	    			patient["observed_age_over_50"] = 0

	    		bmi = float(row[5])
	    		if (bmi >= 25 and bmi <=29.9):
	    			patient["observed_overweight_BMI"] = 1
	    			patient["observed_obese_BMI"] = 0
	    			overweight_BMI += 1
	    		elif (bmi >29.9):
	    			patient["observed_overweight_BMI"] = 0
	    			patient["observed_obese_BMI"] = 1
	    			obese_BMI += 1
	    		else:
                            if (not bmi == 0.0):
	    			patient["observed_overweight_BMI"] = 0
	    			patient["observed_obese_BMI"] = 0

	    		blood_pressure = float(row[2])
	    		if (blood_pressure >= 80):
	    			patient["observed_high_blood_pressure"] = 1
	    			high_blood_pressure += 1
	    		else:
                            if not (blood_pressure == 0.0):
	    			patient["observed_high_blood_pressure"] = 0

	    		diabetes = int(row[8])
	    		patient["observed_diabetes"] = diabetes

	    		skin_thickness = int(row[3])
	    		if (skin_thickness >= 30):
	    			patient["observed_skin_thickness"] = 1
	    		else:
                            if not (skin_thickness == 0.0):
	    			patient["observed_skin_thickness"] = 0


	    		if (num_data > 0):
	    			result.append(patient)
	    			num_data -= 1

	    return result, [variable/len(result) for variable in age_35_to_49, age_over_50, high_blood_pressure, obese_BMI, overweight_BMI, pregnant]

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
num_data = 800 # how many data points you want to put in your observedData list
num_test_data = 20
tempAll = parseData(result, num_data)
temp = tempAll[0]
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

print(len(final_result), tempAll[1])
print(transform_to_string(final_result))
print(transform_to_string(final_test))
print(patient_data)
