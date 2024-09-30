nums = [0, 1, 2, 4, 5, 7]
strn = []

start = nums[0]

for i in range(1, len(nums) + 1):
    if i == len(nums) or nums[i] != nums[i - 1] + 1:
        if start == nums[i - 1]:
            strn.append(str(start))
        else:
            strn.append(f"{start}->{nums[i - 1]}")
        if i < len(nums):
            start = nums[i]

print(strn)