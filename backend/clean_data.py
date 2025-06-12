import pandas as pd
import os

input_folder = '../archive'
output_folder = '../archive/cleaned_financial_data'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.csv') and 'Financial' in filename:
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path)

        # Clean data
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)

        # Try to convert date column if it exists
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='ignore')

        # Save cleaned file
        output_path = os.path.join(output_folder, f'cleaned_{filename}')
        df.to_csv(output_path, index=False)
        print(f'✔️ Cleaned and saved: {output_path}')