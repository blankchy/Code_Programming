import random
import string

def random_string(length:int) -> str:
    string_result = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return string_result