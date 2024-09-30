nums = [3,2,1,1]

if len(nums) <= 2:
    print(max(nums))

nums = sorted(set(nums))
print(nums[len(nums)-3])