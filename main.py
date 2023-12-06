import random
import string
from string import ascii_letters

list1 = []
list2 = []
list3 = []
password = ''
user1 = int(input("how many digits do you want for password?"))
for digits in range(user1):
    digits = list1.append(random.choice(string.digits))

user2 = int(input("how many symbols do you want for password?"))
for symbols in range(user2):
    symbols = list2.append(random.choice(string.punctuation))

user3 = int(input("how many chars do you want for password?"))
for chars in range(user3):
    chars = list3.append(random.choice(string.ascii_letters))

key = list1 + list2 + list3
random.shuffle(key)
for i in key:
    password += i
print(password)
