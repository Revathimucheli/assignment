# -*- coding: utf-8 -*-
"""clean2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MbmksvywWgXTGTfH6qG5c7wxzDeV109d
"""

import pandas as pd
import os

# Ensure data_clean directory exists
os.makedirs("data_clean", exist_ok=True)

# Load dataset
file_path = "/content/StudentsPerformance.csv"
df = pd.read_csv(file_path)

# Standardize column names (lowercase and replace spaces with underscores)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fill missing numerical values with the mean
for col in df.select_dtypes(include=["number"]).columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Save cleaned dataset
cleaned_file_path = "/content/cleaned_student_performance.csv"
df.to_csv(cleaned_file_path, index=False)

print("✅ Data cleaning complete. Missing values replaced with mean. Cleaned data saved at:", cleaned_file_path)