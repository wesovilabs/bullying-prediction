from hrprediction.candidate import Candidate
import csv

NUM_RECORDS = 10000
TRAIN_DATA_FILE_PATH='./../data/input_data.csv'



def generate_array_of_candidates(iterations = NUM_RECORDS):
    candidates_array = [None] * NUM_RECORDS

    for r in range(iterations):
        candidate = Candidate()
        candidate \
            .with_position() \
            .with_genre() \
            .with_years_of_experience() \
            .with_age() \
            .with_desired_salary() \
            .with_previous_companies() \
            .with_type_of_job() \
            .with_interview_results() \
            .with_offer()
        candidates_array[r] = candidate.__dict__
    return candidates_array



def main():
    candidates = generate_array_of_candidates()
    with open(TRAIN_DATA_FILE_PATH, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Position","Genre","Age","Nationality", "Needs to be relocated","Years of experience","Number of previous companies","Desired salary","Interested in freelance positions","Interested in permanent positions","Human resource score","Tech score","Exam score","Average score","Offer","Hired"])
        writer.writerows(
            (
                candidate['position'],
                candidate['genre'],
                candidate['age'],
                candidate['nationality'],
                candidate['needs_relocation'],
                candidate['years_of_experience'],
                candidate['previous_companies'],
                candidate['desired_salary'],
                candidate['freelance'],
                candidate['permanent'],
                candidate['hr_score'],
                candidate['tech_score'],
                candidate['exam_score'],
                candidate['avg_score'],
                candidate['offer'],
                candidate['hired'],

            )
            for candidate in candidates
        )



if __name__ == "__main__":
    main()