import pandas as pd

def analyze_data(dataset_path, column_name):
    # Load the dataset
    df = pd.read_csv(dataset_path)

    # Display the first few rows of the dataframe
    print(df.head())

    # Basic statistics for numerical columns
    print(df.describe())

    # Count of unique values for each column
    for col in df.columns:
        print(f"{col}: {df[col].nunique()} unique values")

    # Count of each unique value in the column
    print(df[column_name].value_counts())

    # Count of each unique value in each column
    for col in df.columns:
        print(f"\nCount of unique values for {col}:")
        print(df[col].value_counts())

if __name__ == "__main__":
    dataset_path = input("Enter your dataset path: ")
    column_name = input("Enter the column name: ")

    analyze_data(dataset_path, column_name)
