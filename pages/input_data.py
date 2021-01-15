import random
from mimesis import Person


class RandomUserData():
    phone = "63" + str(random.randint(1000000, 9999999))
    person = Person('uk')
    name = person.name()
    surname = person.surname()
    promokod = "ABRAKADABRA"


# check working github