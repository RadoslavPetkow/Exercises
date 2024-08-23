def intersection_of_arrays(nums):
    intersection_set = set(nums[0])

    for arr in nums[1:]:
        intersection_set &= set(arr)

    result = sorted(intersection_set)

    return result