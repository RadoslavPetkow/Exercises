import bisect
nums = [1,3,6]
target = 5
x = 0
"You must write an algorithm with O(log n) runtime complexity."
if target in nums:
    x = nums.index(target)
else:
    x = bisect.bisect_left(nums, target)



print(x)