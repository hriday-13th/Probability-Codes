# Random Password Generator:
# Write a program that generates random passwords of a specified length using a mix of letters (both uppercase and
# lowercase), numbers, and special characters. You can define the probability distribution of each character type.

import random
# Uppercase letters ASCII: 65-90
upp_letters = [chr(x) for x in range(65, 91)]

# Lowercase letters ASCII: 97-122
low_letters = [chr(x) for x in range(97, 123)]

# Characters
chars = ['!', '@', '#', '$', '%', '&']

# Numbers
nums = [str(x) for x in range(0, 10)]

k = int(input("How many characters you want in your password: "))
l = int(input("How many do you want: "))

for a in range(l):
    passwd: str = ''

    for i in range(k):
        test = random.randint(1, 4)

        if test == 1:
            passwd += random.choice(upp_letters)

        elif test == 2:
            passwd += random.choice(low_letters)

        elif test == 3:
            passwd += random.choice(chars)

        else:
            passwd += random.choice(nums)

    print(passwd)
