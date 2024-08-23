def longestConsecutive(nums):
    for i in range(len(nums)):
        if i not in nums:
            print(i)

nums = [100,4,200,1,3,2]
longestConsecutive(nums)
