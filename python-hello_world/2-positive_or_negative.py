#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    f'{number} is positive'
elif number == 0:
    f'{number} is 0'
else:
    f'{number} is negative'
    