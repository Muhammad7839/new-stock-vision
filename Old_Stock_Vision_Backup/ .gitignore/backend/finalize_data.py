import pandas as pd
import os

input_folder = '../archive/cleaned_financial_data'

# Combine 2014–2017 files into one training DataFrame
train_df = pd.DataFrame()
for filename in os.listdir(input_folder):
    if filename.endswith('.csv') and '2018' not in filename:
        print("Reading:", filename)
        file_path = os.path.join(input_folder, filename)
        df = pd.read_csv(file_path, header=0)
        print("Shape of", filename, ":", df.shape)
        year = filename.split('_')[1]
        df['Year'] = year
        train_df = pd.concat([train_df, df], ignore_index=True)
train_df.drop_duplicates(inplace=True)

# Convert columns with 'date' in their name to datetime
for col in train_df.columns:
    if 'date' in col.lower():
        train_df[col] = pd.to_datetime(train_df[col], errors='coerce')

# Load and clean the 2018 test data
test_path = os.path.join(input_folder, 'cleaned_2018_Financial_Data.csv')
test_df = pd.read_csv(test_path, header=0)
test_df['Year'] = '2018'
# test_df.dropna(inplace=True)
test_df.drop_duplicates(inplace=True)
for col in test_df.columns:
    if 'date' in col.lower():
        test_df[col] = pd.to_datetime(test_df[col], errors='coerce')

# Clean column names
def clean_column_names(df):
    df.columns = df.columns.str.strip().str.replace('[^A-Za-z0-9_]+', '_', regex=True)
    return df

train_df = clean_column_names(train_df)
test_df = clean_column_names(test_df)

# Make sure the output folder exists and save the files
os.makedirs('../archive/financial_data', exist_ok=True)
train_df.to_csv('../archive/financial_data/final_training_data.csv', index=False)
print('Final training dataset saved as final_training_data.csv')
print("train_df shape before save:", train_df.shape)
print(train_df.head())

test_df.to_csv('../archive/financial_data/final_testing_data.csv', index=False)
print('Final testing dataset saved as final_testing_data.csv')
print("test_df shape before save:", test_df.shape)
print(test_df.head())