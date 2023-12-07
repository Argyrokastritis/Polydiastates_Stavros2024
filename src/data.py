import random
import names


class Scientist(object):
    def __init__(self, s, a, d, e):
        self.surname = s
        self.awards = a
        self.dblp_records = d
        self.education = e



def generate_data(length):
    computer_science_universities = [
        "MIT",
        "Stanford University",
        "Carnegie Mellon University",
        "UC Berkeley",
        "Princeton University",
        "Harvard University",
        "Caltech",
        "Cornell University",
        "University of Chicago",
        "Columbia University",
        "New York University",
        "Rice University",
        "University of Texas - Austin",
        "University of Illinois - Urbana-Champaign",
        "University of Maryland - College Park",
        "University of Pennsylvania",
        "Yale University",
        "Cambridge",
        "Berkley",
        "Oxford University",
        "Johns Hopkins University",
        "University of College London",
        "Tsinghua University",
        "Ohio State University",
        "University of Tokyo",
        "National University of Singapore",
        "University of Pittsburgh",
        "McGill University",
        "Nanyang Technological University",
        "University of Melbourne",
        "Catholic University of Leuven",
        "University of Sydney",
        "Shanghai Jiao Tong University"
    ]

    scientists = []
    used_surnames = []
    for i in range(length):
        surname = names.get_last_name().lower()
        while surname in used_surnames:
            surname = names.get_last_name().lower()
        used_surnames.append(surname)
        awards = random.randint(0, 30)
        dblp_records = random.randint(0,200)
        education = random.sample(computer_science_universities, 5)
        scientist = Scientist(surname, awards, dblp_records, education)
        scientists.append(scientist)
        # print(scientist.dblp_records)
    return scientists
