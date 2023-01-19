
from typing import Tuple
import random
import string

def generate_random_word(word_length) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=word_length))

def generate_random_number(number_digits) -> str:
    return ''.join(random.choices(string.digits, k=number_digits))

def generate_data_row(number_digits: int = 4, word_length: int = 12) -> Tuple[str, str]:
    return generate_random_number(number_digits), generate_random_word(word_length)