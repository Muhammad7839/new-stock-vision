import pandas as pd
import os

# This script cleans all yearly financial data files for the project.
# It fills missing values with 0 (instead of dropping rows), removes duplicates, and saves the cleaned files.
# It also prints a summary for each file for transparency.

input_folder = '../archive'
output_folder = '../archive/cleaned_financial_data'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.csv') and 'Financial' in filename:
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path)

        # Summary before cleaning
        n_rows_before = len(df)
        n_missing_before = df.isnull().sum().sum()

        # Fill missing values with 0 for consistency
        df.fillna(0, inplace=True)
        df.drop_duplicates(inplace=True)

        # Try to convert date column if it exists
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='ignore')

        # Summary after cleaning
        n_rows_after = len(df)
        n_missing_after = df.isnull().sum().sum()

        # Save cleaned file
        output_path = os.path.join(output_folder, f'cleaned_{filename}')
        df.to_csv(output_path, index=False)

        print(f'✔️ Cleaned and saved: {output_path}')
        print(f'   Rows before: {n_rows_before}, after: {n_rows_after}. Missing values filled: {n_missing_before - n_missing_after}')