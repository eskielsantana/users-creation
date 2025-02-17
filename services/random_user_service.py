import os
import re

from services.random_data import symbols, first_names, last_names, locations
from utils.faker import Faker
from utils.string_utils import remove_accent


def random_phone_number(country_code, area_codes):
    if country_code != "55":
        segment1 = Faker.int(100, 999)
        segment2 = Faker.int(1000, 9999)
        return f"+{country_code} ({Faker.choice(area_codes)}) {segment1}-{segment2}"

    segment1 = Faker.int(9000, 9999)
    segment2 = Faker.int(1000, 9999)
    return f"+{country_code} ({Faker.choice(area_codes)}) 9{segment1}-{segment2}"


def random_email(first_name, last_name):
    first_name = remove_accent(first_name.lower())
    last_name = remove_accent(last_name.lower())
    joint_first_name = re.sub(r'\s', Faker.choice(symbols), first_name)
    joint_last_name = re.sub(r'\s+', Faker.choice(symbols), last_name)

    email = ""
    symbol = ""
    initials = ""

    switch = Faker.int(0, 9)
    if switch in [0, 1]:
        # ezequiel.santana / ezequiel_santana
        symbol = '.' if Faker.chance(50) else '_'
        email = f"{joint_first_name}{symbol}{joint_last_name}"
    elif switch in [2, 3]:
        # e.santana / e_santana
        symbol = '.' if Faker.chance(50) else '_'
        email = f"{joint_first_name[0]}{symbol}{joint_last_name}"
    elif switch in [4, 5]:
        # ezequiel.sj / eskiel_sj
        initials = ''.join([word[0] for word in last_name.split()])
        symbol = '.' if Faker.chance(50) else '_'
        email = f"{joint_first_name}{symbol}{initials}"
    elif switch in [6, 7]:
        # eze.santana / eze_santana
        initials = joint_first_name[:3] if len(joint_first_name) > 5 else joint_first_name
        symbol = '.' if Faker.chance(50) else '_'
        email = f"{initials}{symbol}{joint_last_name}"
    else:
        # ezequiel3232
        rnd_number = Faker.int(100, 9999)
        email = f"{joint_first_name}{rnd_number}"

    return f"{email}@automation.com"


class RandomUserService:
    def __init__(self):
        self.defaultPass = os.getenv('DEFAULT_PASS')

    def create(self):
        first_name = Faker.choice(first_names)
        last_name = Faker.choice(last_names)
        email = random_email(first_name, last_name)
        location = Faker.choice(locations)

        return {
            "email": email,
            "password": self.defaultPass,
            "first_name": first_name,
            "last_name": last_name,
            "avatar": None,
            "city": location['city'],
            "region": location['region'],
            "country": location['country'],
            "address1": location['address1'],
            "address2": location['address2'],
            "post_code": location['post_code'],
            "phone1": random_phone_number(location['phone_country_code'], location['phone_area_codes']),
            "phone2": random_phone_number(location['phone_country_code'], location['phone_area_codes']),
            "division": "",
            "notes": "User auto generated.",
            "roles": [
                111
            ],
            "company": 5,
            "qualifications": [9],
            "supervisor": 58,
            "employee_id": None,
            "user_tier": "Office User"
        }
