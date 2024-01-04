import pandas as pd

# Load the dataset
dataset_path = 'your_dataset_path_here'  # replace with your dataset path
df = pd.read_csv(dataset_path)

# Display the first few rows of the dataframe
print(df.head())

# Basic statistics for numerical columns
print(df.describe())

# Count of unique values for each column
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Replace 'your_column_name_here' with your column name
column_name = 'your_column_name_here'
print(df[column_name].value_counts())

# Count of each unique value in each column
for col in df.columns:
    print(f"\nCount of unique values for {col}:")
    print(df[col].value_counts())
