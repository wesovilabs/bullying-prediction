import numpy as np
import pandas as pd


TRAIN_DATA_DIR_PATH='./../data/train/'
TEST_DATA_DIR_PATH='./../data/test/'

RANGES = [
    'RANGE_9_11_WOMEN',
    'RANGE_12_13_WOMEN',
    'RANGE_14_16_WOMEN',
    'RANGE_9_11_MEN',
    'RANGE_12_13_MEN',
    'RANGE_14_16_MEN',
]



def csv_to_data_frame(range):
    return pd.read_csv(TRAIN_DATA_DIR_PATH+range.lower()+'_train_data.csv')



def main():
    for range in RANGES:
        df = csv_to_data_frame(range)
        index = 10
        size=10
        df = df[index:index+size]
        df.to_csv(TEST_DATA_DIR_PATH + range.lower() + '_test_data.csv', sep=',', encoding='utf-8', header=True,
                  index=False)

if __name__ == "__main__":
    main()