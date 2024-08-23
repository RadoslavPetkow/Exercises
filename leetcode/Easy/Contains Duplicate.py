checking_list = []
nums = [int(x) for x in input().split(",")]

for x in nums:
    if x in checking_list:
        print(True)
        exit(0)
    else:
        checking_list.append(x)
print(False)

