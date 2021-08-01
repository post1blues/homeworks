import random

input_string = input("Enter you string: ").strip()

for _ in range(5):
    chars = list(input_string)
    random.shuffle(chars)
    print(''.join(chars))
