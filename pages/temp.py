from mimesis import Person
import random

person = Person('uk')
name = person.name()
email = person.email()
surname = person.surname()
phone = int("63" + str(random.randint(1000000, 9999999)))

print(name)
print(surname)
print(phone)
print(person)
print(email)