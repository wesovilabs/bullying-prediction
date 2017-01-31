import csv

from utils.bullying import Bullying

NUM_RECORDS = 10000000
INPUT_DATA_FILE_PATH= './../data/input_data.csv'

def generate_array(iterations = NUM_RECORDS):
    array = [None] * NUM_RECORDS

    for r in range(iterations):
        bullying = Bullying()
        bullying \
            .age() \
            .genre() \
            .short() \
            .wear_braces() \
            .wear_glasses() \
            .less_popular() \
            .different_race() \
            .low_socioeconomic_status() \
            .gay_or_lesbian() \
            .have_disability() \
            .overweight() \
            .shy() \
            .affected()
        array[r] = bullying.__dict__
    return array



def main():
    bullying_array = generate_array()
    with open(INPUT_DATA_FILE_PATH, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Range","Is short","shy","Wear braces","Wear glasses","Is less popular", "Different race", "Low socioeconomic status","Gay or lesbian",
                         "Have disability", "Overweight", "Genre", "Age", "Suffer from bullying"])
        writer.writerows(
            (
                bullying['range'],
                bullying['short'],
                bullying['shy'],
                bullying['wear_braces'],
                bullying['wear_glasses'],
                bullying['less_popular'],
                bullying['different_race'],
                bullying['low_socioeconomic_status'],
                bullying['gay_or_lesbian'],
                bullying['have_disability'],
                bullying['overweight'],
                bullying['genre'],
                bullying['age'],
                bullying['affected'],
            )
            for bullying in bullying_array
        )



if __name__ == "__main__":
    main()