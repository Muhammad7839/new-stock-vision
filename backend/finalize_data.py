import pandas as pd
import os

input_folder = '../archive/cleaned_financial_data'

# ✅ Step A: Create Training Dataset (2014–2017)
train_df = pd.DataFrame()

for filename in os.listdir(input_folder):
    if filename.endswith('.csv') and '2018' not in filename:
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path, header=0)
        year = filename.split('_')[0]
        df['Year'] = year
        train_df = pd.concat([train_df, df], ignore_index=True)

# Clean it further just in case
train_df.dropna(inplace=True)
train_df.drop_duplicates(inplace=True)

for col in train_df.columns:
    if 'date' in col.lower():
        train_df[col] = pd.to_datetime(train_df[col], errors='coerce')

# ✅ Step B: Create Testing Dataset (2018 only)
test_path = os.path.join(input_folder, 'cleaned_2018_Financial_Data.csv')
test_df = pd.read_csv(test_path, header=0)
test_df['Year'] = '2018'

test_df.dropna(inplace=True)
test_df.drop_duplicates(inplace=True)

for col in test_df.columns:
    if 'date' in col.lower():
        test_df[col] = pd.to_datetime(test_df[col], errors='coerce')

def clean_column_names(df):
    df.columns = df.columns.str.strip().str.replace('[^A-Za-z0-9_]+', '_', regex=True)
    return df

train_df = clean_column_names(train_df)
test_df = clean_column_names(test_df)

train_df.to_csv('../archive/final_training_data.csv', index=False)
print('✅ Final training dataset saved as final_training_data.csv')

test_df.to_csv('../archive/final_testing_data.csv', index=False)
print('✅ Final testing dataset saved as final_testing_data.csv')