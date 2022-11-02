import pandas as pd
table = pd.read_json('BMI.json')

# Calculation of BMI

def BMI_Calculate(x,y) :
    WeightKg=x
    HeightCm=y
    BMI = WeightKg / ((HeightCm/100) ** 2)
    return BMI

# Comparison of calculated BMI against Category and associated Health Risk

def Compare(x):
    BMI = x
    if BMI <= 18.4:
        BMI_Category = 'Underweight'
        Health_Risk = 'Malnutrition Risk'
    elif (BMI <= 24.9):
        BMI_Category = 'Normal Weight'
        Health_Risk = 'Low Risk'
    elif (BMI <= 29.9):
        BMI_Category = 'Overweight'
        Health_Risk = 'Enhanced Risk'
    elif (BMI <= 34.9):
        BMI_Category = 'Moderately Obese'
        Health_Risk = 'Medium Risk'
    elif (BMI <= 39.9):
        BMI_Category = 'Severely Obese'
        Health_Risk = 'High Risk'
    else:
        BMI_Category = 'Very Severely Obese'
        Health_Risk = 'Very High Risk'
    return BMI_Category, Health_Risk

# Adding new columns to table

table['BMI'] = BMI_Calculate(table['WeightKg'], table['HeightCm'])
table['BMI_Cat'] = table['BMI'].apply(Compare)
table[['BMI_Category', 'Health_Risk']] = pd.DataFrame(table['BMI_Cat'].tolist(), index=table.index)
table.drop('BMI_Cat', axis=1, inplace=True)
print(table)

# Number of Overweight People

n_overweight = len(table[table['BMI_Category'] == 'Overweight'])
print ("Number of overweight people = ", n_overweight );
