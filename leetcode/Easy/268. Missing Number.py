"""soo this is my solution but is O(n2) so i asked ChatGPT(MY BEST FRIEND) to give me better solution which is just O(n)
feeling so dumb.Its understandable im not an asian """
nums = [0,1]
for i in range(len(nums)+1):
    if i not in nums:
        print(i)

"""class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2 
        actual_sum = sum(nums)  
        return total_sum - actual_sum  """