num = 1
nums = []
while True:
    if num > 100:
        break
    nums.append(num)
    num += 1

idx = 0
result_list = []
while idx < len(nums):
    if nums[idx] % 7 == 0 and nums[idx] % 5 != 0:
        result_list.append(nums[idx])
    idx += 1

print(result_list)