from collections import Counter

nums = [2,2,1]
counter = Counter(nums)
duplicates = [item for item, count in counter.items() if count == 1]
print(duplicates)