import random

list_1 = []
list_2 = []

while len(list_1) < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

list_3 = list(set(list_1).intersection(list_2))

print(' '.join([str(num) for num in list_3]))
