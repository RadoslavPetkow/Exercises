nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = nums1[:m]
nums2 = nums2[:n]

nums1.extend(nums2)
print(sorted(nums1))
'dont work in func cuz i dont modify the original one , only the local'
'under is the Chatgpt answer ,programing is not logical as i want '

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Modify nums1 in-place by merging nums2 into it.
        """
        # Start filling nums1 from the last index
        last = m + n - 1  # Last index of the merged array

        # Pointers for nums1 and nums2
        i = m - 1  # Last element in nums1's original part
        j = n - 1  # Last element in nums2

        # Merge nums1 and nums2 starting from the back
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1

        # If there are any remaining elements in nums2, copy them
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1