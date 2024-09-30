nums = [0,1,0,3,12]
counter = 0

while True:
    if 0 in nums:
        counter +=1
        nums.remove(0)
    else:
        break

for i in range(counter):
    nums.append(0)

print(nums)
