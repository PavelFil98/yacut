import random
import string


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(letters_and_digits, k=6))
    return short_url