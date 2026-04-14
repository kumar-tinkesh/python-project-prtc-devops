import datetime, random


# getting a list of number random objects
def getBirthDays(numberOfBirthDays):
    birthdays = []

    for i in range(numberOfBirthDays):
        # year is unimportant if two birthdays have same year
        startOfYear = datetime.date(2020,1,1)

        # getting a random day
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        # creating a birthdate by adding two
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    
    return birthdays


def getMatch(birthdays):
    """
    return the date object of a birthday that occurs more than once in a birthdays
    """
    if len(birthdays)  == len(set(birthdays)):
        # all birthdays are uniue so return None
        return None
    
    #  comparing birthday to eac other
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                # return the matching one
                return birthdayA



print(""". ...Birthday Paradox... .
        The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
""")


MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul','Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthday do you want to generate.. .")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print("Here are", numBDays, "birthdays: ")
birthdays = getBirthDays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end="")