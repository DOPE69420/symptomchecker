import pandas as pd

# 4 CSV files load kar rahe hain
dataset = pd.read_csv("dataset.csv")
symptom_severity = pd.read_csv("Symptom-severity.csv")
symptom_description = pd.read_csv("symptom_Description.csv")
symptom_precaution = pd.read_csv("symptom_precaution.csv")

# Print karke dekhne ke liye
print(dataset.head())
print(symptom_severity.head())
print(symptom_description.head())
print(symptom_precaution.head())
