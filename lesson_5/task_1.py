import random

nums = []
while len(nums) < 10:
    nums.append(random.randint(1, 100))

print(f"Max num in list: ", max(nums))