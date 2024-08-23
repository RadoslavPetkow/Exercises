nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

print([list(set(nums1) - set(nums2)),list(set(nums2) - set(nums1))])