import numpy as np
import pandas as pd
import os


INPUT_DATA_FILE_PATH='./../data/input_data.csv'
TRAIN_DATA_DIR_PATH='./../data/train/'

RANGES = [
    'RANGE_9_11_WOMEN',
    'RANGE_12_13_WOMEN',
    'RANGE_14_16_WOMEN',
    'RANGE_9_11_MEN',
    'RANGE_12_13_MEN',
    'RANGE_14_16_MEN',
]

def normalize_genre(genre_string):
    return  [0,1][genre_string == 'Male']

def normalize_input_data(df):
    df['Genre'] = df['Genre'].apply(normalize_genre)
    return df

def remove_useless_columns_and_save_train_data(df, range, output_file=TRAIN_DATA_DIR_PATH):
    df = df.drop('Age', 1)
    df = df.drop('Genre', 1)
    dataframes = np.array_split(df, 25)
    if not os.path.exists(output_file+range.lower()):
        os.makedirs(output_file+range.lower())
    for i, dataframe in enumerate(dataframes):
        dataframe.to_csv(output_file+range.lower()+'/'+str(i)+'.csv', sep=',', encoding='utf-8', header=True, index=False)


def csv_to_data_frame(input_file):
    return pd.read_csv(input_file,
        dtype={
            'Range': str,
            'Wear glasses': np.int32,
            'Is short': np.int32,
            'Wear braces': np.int32,
            'Is less popular': np.int32,
            'Different race': np.int32,
            'Low socioeconomic status': np.int32,
            'Gay or lesbian': np.int32,
            'Have disability': np.int32,
            'Overweight': np.int32,
            'shy': np.int32,
        }
    )

def read_input_data(input_file=INPUT_DATA_FILE_PATH):
    return csv_to_data_frame(input_file)

def preparing_train_data(range):
    df = read_input_data()
    # Filtering records by age,genre range
    df = df[df['Range'] == range]
    # Removing useless columns
    df.drop('Range', axis=1, inplace=True)
    df = normalize_input_data(df)
    remove_useless_columns_and_save_train_data(df,range)

def main():
    for range in RANGES:
        preparing_train_data(range)

if __name__ == "__main__":
    main()