import random

GENRE = {
    'F': 'Female',
    'M': 'Male'
}


RANGE_9_11_MEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}

RANGE_9_11_WOMEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}

RANGE_12_13_MEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}

RANGE_12_13_WOMEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}

RANGE_14_16_MEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}

RANGE_14_16_WOMEN = {
    'wear_glasses':random.choice(range(1,10)),
    'short':random.choice(range(1,10)),
    'wear_braces':random.choice(range(1,10)),
    'less_popular':random.choice(range(1,10)),
    'different_race':random.choice(range(1,10)),
    'low_socioeconomic_status':random.choice(range(1,10)),
    'gay_or_lesbian':random.choice(range(1,10)),
    'have_disability':random.choice(range(1,10)),
    'overweight':random.choice(range(1,10)),
    'shy':random.choice(range(1,10)),
}





def normalize_input_percentages(factors,higher_risk_factor):
    accum = sum(factors.values())
    pending_to_assign = 100 - accum
    rest = pending_to_assign % 10
    factors[higher_risk_factor]+=rest
    extra_value = (pending_to_assign-rest)/10
    return list(map((lambda x: x + extra_value), factors.values()))

class Bullying(object):

    def age(self):
        self.age = random.choice(range(9, 16))
        return self

    def genre(self):
        self.genre = random.choice([GENRE['F'], GENRE['M']])
        return self

    def short(self):
        self.short = (int)(random.random() < 0.3)
        return self

    def wear_braces(self):
        self.wear_braces = (int)(random.random() < 0.3)
        return self

    def wear_glasses(self):
        self.wear_glasses = (int)(random.random() < 0.7)
        return self

    def less_popular(self):
        self.less_popular = (int)(random.random() < 0.6)
        return self

    def different_race(self):
        self.different_race = (int)(random.random() < 0.1)
        return self

    def low_socioeconomic_status(self):
        self.low_socioeconomic_status = (int)(random.random() < 0.5)
        return self

    def gay_or_lesbian(self):
        self.gay_or_lesbian = (int)(random.random() < 0.2)
        return self

    def have_disability(self):
        self.have_disability = (int)(random.random() < 0.3)
        return self

    def overweight(self):
        self.overweight = (int)(random.random() < 0.6)
        return self

    def shy(self):
        self.shy = (int)(random.random() < 0.3)
        return self


    def affected(self):
        min_risk = 15
        if self.genre is "Female":
            if self.age <= 11:
                self.range ='RANGE_9_11_WOMEN'
                current_range = RANGE_9_11_WOMEN
                min_risk=33
            elif self.age <= 13:
                self.range = 'RANGE_12_13_WOMEN'
                current_range = RANGE_12_13_WOMEN
                min_risk = 28
            else:
                self.range = 'RANGE_14_16_WOMEN'
                current_range = RANGE_14_16_WOMEN
                min_risk = 21
        else:
            if self.age <= 11:
                self.range = 'RANGE_9_11_MEN'
                min_risk = 28
                current_range = RANGE_9_11_MEN
            elif self.age <= 13:
                self.range = 'RANGE_12_13_MEN'
                min_risk = 24
                current_range = RANGE_12_13_MEN
            else:
                self.range = 'RANGE_14_16_MEN'
                min_risk = 16
                current_range = RANGE_14_16_MEN
        risk_percentage = \
            self.short * current_range['short']+ \
            self.wear_braces * current_range['wear_braces'] + \
            self.wear_glasses * current_range['wear_glasses'] + \
            self.less_popular * current_range['less_popular'] + \
            self.different_race * current_range['different_race'] + \
            self.low_socioeconomic_status * current_range['low_socioeconomic_status'] + \
            self.gay_or_lesbian * current_range['gay_or_lesbian'] + \
            self.have_disability * current_range['have_disability'] + \
            self.overweight * current_range['overweight'] + \
            self.shy * current_range['shy'];
        self.affected=(int) (risk_percentage > min_risk)
        return self


value = normalize_input_percentages(RANGE_9_11_MEN, 'overweight')
print(value)

bullying = Bullying()
bullying \
    .age() \
    .genre() \
    .short()\
    .wear_braces() \
    .wear_glasses() \
    .less_popular() \
    .different_race() \
    .low_socioeconomic_status() \
    .gay_or_lesbian() \
    .have_disability() \
    .overweight() \
    .shy()\
    .affected()
