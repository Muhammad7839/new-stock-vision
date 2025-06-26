import pandas as pd
import os

input_dir = 'archive/financial_data'
output_dir = 'archive/cleaned_financial_data'
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_dir, filename)
        df = pd.read_csv(file_path)

        # 1. Fill missing values with 0 (instead of dropping)
        df.fillna(0, inplace=True)

        # 2. Remove duplicate rows
        df.drop_duplicates(inplace=True)

        # 3. Fix datetime columns if needed
        for col in df.columns:
            if 'date' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col], errors='coerce')
                except Exception:
                    pass

        # 4. Save the cleaned file
        cleaned_path = os.path.join(output_dir, f'cleaned_{filename}')
        df.to_csv(cleaned_path, index=False)

        print(f'✅ Cleaned and saved: {cleaned_path}')
        print(f'   Rows after cleaning: {len(df)}\n')