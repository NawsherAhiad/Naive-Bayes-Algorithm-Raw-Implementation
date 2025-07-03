# Naive Bayes Classifier Implementation
# This code implements a Naive Bayes classifier for a dataset with categorical features.
import pandas as pd
import numpy as np

#Load dataset
df = pd.read_csv("/mnt/data/Naive Bayes Dataset - Sheet1 (1).csv")
df_yes = df[df['deposit'] == 'yes']
df_no = df[df['deposit'] == 'no']

#Basic statistics
total_rows = len(df)
yes_size = len(df_yes)
no_size = len(df_no)

# Extract unique values and category sizes
unique_list_total = [len(df[col].unique()) for col in df.columns]
value = [df[col].unique() for col in df.columns]

#Define the categorical columns to analyze
column = ['marital status', 'education status', 'housing', 'loan']

#Frequency tables for "yes"
arr_yes = []
for col in column:
    counts = []
    for val in df[col].unique():
        counts.append(len(df_yes[df_yes[col] == val]))
    arr_yes.append(counts)

#Frequency tables for "no"
arr_no = []
for col in column:
    counts = []
    for val in df[col].unique():
        counts.append(len(df_no[df_no[col] == val]))
    arr_no.append(counts)

#Load test dataset
df_test = pd.read_csv("/mnt/data/test.csv")
df_test.drop(columns=['SL'], inplace=True)

#Multiplication helper
def mul(arr):
    result = 1
    for val in arr:
        result *= val
    return result

#Merged conditional probability calculation
NB_yes = []
NB_no = []

def cond_matching(brr, arr, size, class_label):
    calculate = []
    for i in range(len(df_test.columns)):
        for j in range(unique_list_total[i + 1]):
            if brr[i] == value[i + 1][j]:
                prob = (arr[i][j] + 1) / (size + unique_list_total[i + 1])
                calculate.append(prob)
                break
    result = mul(calculate) * (size / total_rows)
    if class_label == "yes":
        NB_yes.append(result)
    else:
        NB_no.append(result)

#Run prediction loop
inputt = []
for i in range(len(df_test)):
    brr = [df_test.iloc[i, j] for j in range(len(df_test.columns))]
    cond_matching(brr, arr_yes, yes_size, "yes")
    cond_matching(brr, arr_no, no_size, "no")
    inputt.append(brr)

#Final predictions
predictions = []
for y_prob, n_prob in zip(NB_yes, NB_no):
    predictions.append("yes" if y_prob > n_prob else "no")

#Output predictions
for i, pred in enumerate(predictions):
    print(f"Test instance {i+1}: Predicted -> {pred}")
