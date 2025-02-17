import random
import string
import uuid


class Faker(object):
    @classmethod
    def uuid4(cls):
        return str(uuid.uuid4())

    @classmethod
    def first_name(cls):
        return cls.first_letter_upper(cls.get_random_string(20))

    @classmethod
    def last_name(cls):
        return cls.first_letter_upper(cls.get_random_string(20))

    @classmethod
    def word(cls):
        return cls.first_letter_upper(cls.get_random_string(12))

    @classmethod
    def text(cls, max_nb_chars=20):
        return cls.first_letter_upper(cls.get_random_string(max_nb_chars))

    @classmethod
    def hex_color(cls):
        return "#{0}".format(("%x" % random.randint(1, 16777215)).ljust(6, '0'))  # NOQA S311

    @classmethod
    def url(cls):
        return 'www.' + cls.get_random_string(20) + '.com'

    @classmethod
    def company(cls):
        return cls.first_letter_upper(cls.get_random_string(20))

    @classmethod
    def address(cls):
        return '1234 ' + cls.get_random_string(12) + ' St'

    @classmethod
    def file_name(cls):
        return cls.get_random_string(20) + '.' + cls.get_random_string(3)

    @classmethod
    def first_letter_upper(cls, text):
        return text[0].upper() + text[1:]

    @staticmethod
    def latitude():
        return str(random.randint(-8999999, 8999999) / 1e5)  # noqa: S311

    @staticmethod
    def longitude():
        return str(random.randint(-179999999, 17999999) / 1e5)  # noqa: S311

    @staticmethod
    def int(a=-1e5, b=1e5):
        return random.randint(a, b)  # noqa: S311

    @staticmethod
    def float(a=-1e10, b=1e10):
        return random.randint(a, b) / 1e5  # noqa: S311

    @staticmethod
    def choice(options):
        return options[random.randint(0, len(options) - 1)]  # noqa: S311

    @staticmethod
    def chance(percentage):
        return random.random() < percentage / 100

    @staticmethod
    def get_random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(length))
