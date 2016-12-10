import numpy as np
import pandas as pd

INPUT_DATA_FILE_PATH='./../data/input_data.csv'
TRAIN_DATA_FILE_PATH='./../data/train_data.csv'

POSITION = {
    'SOLUTION_ARCHITECT':'Solution architect',
    'DEVOPS': 'Devops',
    'SOFTWARE_ENGINEER': 'Software engineer',
    'SOFTWARE_DEVELOPER': 'Software developer',
    'SOFTWARE_ARCHITECT': 'Software architect',
    'CTO': 'CTO',
    'SYSOPS': 'Sysops',
    'SM': 'Scrum master',
    'PO': 'Product owner',
}

def normalize_genre(genre_string):
    return  [0,1][genre_string == 'Male']

def normalize_needs_to_be_relocated(needs_to_be_relocated_bool):
    return  [1,0][needs_to_be_relocated_bool]

def normalize_interested_in_freelance_positions(interested_in_freelance_positions):
    return  [1,0][interested_in_freelance_positions]

def normalize_interested_in_permanent_positions(interested_in_permanent_positions):
    return  [1,0][interested_in_permanent_positions]

def normalize_hired(normalize_hired_bool):
    return  [1,0][normalize_hired_bool]

def normalize_score(score):
    return round(score/5,3)

def normalize_salary(salary):
    return round(salary /120000, 3)

def normalize_years(years):
    return round(years/100, 2)

def normalize_position(position_string):

    position_switcher = {
        POSITION['DEVOPS']: 0,
        POSITION['SOFTWARE_ENGINEER']: 0.1,
        POSITION['SOFTWARE_DEVELOPER']: 0.2,
        POSITION['SOFTWARE_ARCHITECT']: 0.3,
        POSITION['CTO']: 0.4,
        POSITION['SYSOPS']: 0.5,
        POSITION['SM']: 0.6,
        POSITION['PO']: 0.7
    }
    return  position_switcher[position_string]

def normalize_input_date(df):

    df['Age'] = df['Age'].apply(normalize_years)
    df['Genre'] = df['Genre'].apply(normalize_genre)
    df['Position'] = df['Position'].apply(normalize_position)
    df['Years of experience'] = df['Years of experience'].apply(normalize_years)
    df['Needs to be relocated'] = df['Needs to be relocated'].apply(normalize_needs_to_be_relocated)
    df['Interested in freelance positions'] = df['Interested in freelance positions'].apply(normalize_interested_in_freelance_positions)
    df['Interested in permanent positions'] = df['Interested in permanent positions'].apply(normalize_interested_in_permanent_positions)
    df['Desired salary'] = df['Desired salary'].apply(normalize_salary)
    df['Number of previous companies'] = df['Number of previous companies'].apply(normalize_salary)


    df['Human resource score'] = df['Human resource score'].apply(normalize_score)
    df['Tech score'] = df['Tech score'].apply(normalize_score)
    df['Exam score'] = df['Exam score'].apply(normalize_score)
    df['Average score'] = df['Average score'].apply(normalize_score)

    df['Offer'] = df['Offer'].apply(normalize_salary)
    df['Hired'] = df['Hired'].apply(normalize_hired)
    return df

def remove_useless_columns_and_save_train_data(df, output_file=TRAIN_DATA_FILE_PATH):
    df = df.drop('Nationality',1)
    df.to_csv(output_file, sep=',', encoding='utf-8', header=False, index=False)


def csv_to_data_frame(input_file):
    return pd.read_csv(input_file,
        dtype={
            "Position":str,
            "Genre":str,
            "Age":np.int32,
            "Nationality":str,
            "Needs to be relocated":np.bool,
            "Years of experience":np.int32,
            "Number of previous companies":np.int32,
            "Desired salary":np.float,
            "Interested in freelance positions":np.bool,
            "Interested in permanent positions":np.bool,
            "Human resource score":np.float,
            "Tech score":np.float,
            "Exam score":np.float,
            "Average score":np.float,
            "Offer":np.float,
            "Hired":np.bool
        }
    )

def remove_useless_records(input_file=INPUT_DATA_FILE_PATH):
    df = csv_to_data_frame(input_file)
    df = df[df['Offer'].notnull()]
    return df

def preparing_train_data():
    df = remove_useless_records()
    df = normalize_input_date(df)
    remove_useless_columns_and_save_train_data(df)

def main():
    preparing_train_data()

if __name__ == "__main__":
    main()