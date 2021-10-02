from string import ascii_lowercase
from string import digits
from string import punctuation
import random

letters_low = ascii_lowercase
letter_upp = ascii_lowercase.upper()
numbers = digits
symbols = punctuation

string = letters_low + letter_upp + numbers + symbols
password = ''.join(random.sample(string, 8))
print(password)