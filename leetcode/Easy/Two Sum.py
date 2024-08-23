class Solution(object):
    def twoSum(self, nums, target):
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_indices and num_indices[complement] != i:
                return [num_indices[complement], i]

            num_indices[num] = i

        return []