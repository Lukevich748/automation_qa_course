import random
from data.data import Person
from faker import Faker


faker_ru = Faker("ru_RU")

def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        datetime=faker_ru.date_between(start_date='-30y', end_date='today').strftime('%d %m %Y'),
        email=faker_ru.email(),
        phone_number=faker_ru.phone_number(),
        age=random.randint(10, 80),
        salary=random.randint(100, 1000),
        department=faker_ru.job(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )