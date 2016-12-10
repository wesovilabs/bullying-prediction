import random

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

GENRE = {
    'F': 'Female',
    'M': 'Male'
}

POSITIONS = [
    POSITION['SOFTWARE_ARCHITECT'],
    POSITION['DEVOPS'],
    POSITION['SOFTWARE_ENGINEER'],
    POSITION['SOFTWARE_DEVELOPER'],
    POSITION['SOFTWARE_ARCHITECT'],
    POSITION['CTO'],
    POSITION['SYSOPS'],
    POSITION['SM'],
    POSITION['PO'],
]

LOCATIONS = ['Spanish', 'Italian', 'French', 'British', 'Irish', 'Indian', 'Turkish', 'Portuguese', 'Brazilian']

class Candidate(object):

    age_switcher = {
        POSITION['DEVOPS']:random.choice(range(4,15)),
        POSITION['SOFTWARE_ENGINEER']:random.choice(range(2,20)),
        POSITION['SOFTWARE_DEVELOPER']:random.choice(range(0,20)),
        POSITION['SOFTWARE_ARCHITECT']:random.choice(range(8,20)),
        POSITION['CTO']:random.choice(range(10,30)),
        POSITION['SYSOPS']:random.choice(range(2,10)),
        POSITION['SM']:random.choice(range(3,30)),
        POSITION['PO']:random.choice(range(8,30))
    }

    desired_salary_switcher = {
        POSITION['SOFTWARE_ARCHITECT']: random.choice(range(40, 75)),
        POSITION['DEVOPS']: random.choice(range(35, 55)),
        POSITION['SOFTWARE_ENGINEER']: random.choice(range(25, 40)),
        POSITION['SOFTWARE_DEVELOPER']: random.choice(range(23, 30)),
        POSITION['CTO']: random.choice(range(60, 90)),
        POSITION['SYSOPS']: random.choice(range(27, 420)),
        POSITION['SM']: random.choice(range(32, 50)),
        POSITION['PO']: random.choice(range(40, 70))
    }

    def __init__(self):
        self.nationality = random.choice(LOCATIONS)
        self.needs_relocation = random.choice([random.choice([True, False]), False])

    def with_position(self):
        self.position = random.choice(POSITIONS)
        return self

    def with_desired_salary(self):
        self.desired_salary = 1000* self.desired_salary_switcher.get(self.position)
        return self

    def with_genre(self):
        self.genre = random.choice([GENRE['F'], GENRE['M']])
        return self

    def with_years_of_experience(self):
        self.years_of_experience = self.age_switcher.get(self.position)
        return self

    def with_age(self):
        self.age= self.years_of_experience + random.choice(range(22,30))
        return self

    def with_previous_companies(self):
        self.previous_companies= random.choice(range(1,self.years_of_experience))
        return self

    def with_type_of_job(self):
        self.freelance = random.choice([random.choice([True,False]),False])
        self.permanent = random.choice([True, False])
        return self

    def with_interview_results(self):
        self.hr_score = random.choice(range(5))
        self.tech_score = random.choice(range(5))
        self.exam_score = random.choice(range(5))
        self.avg_score = float("{0:.2f}".format((self.hr_score+self.tech_score+self.exam_score)/3))

        return self

    def with_offer(self):
        if (self.avg_score >= 1.0):
            self.offer = random.choice(range(800*((int)(self.desired_salary/1000)), self.desired_salary))
            self.hired = random.choice([True, False])
        else:
            self.offer=None
            self.hired=None
        return self

