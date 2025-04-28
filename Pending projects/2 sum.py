nums = [2,7,9,10]
target = 19

l = [nums.index(i) for i in nums]
l1 = []

for i in nums:
    x = i
    
for i in l:
    if nums[i]+nums[i+1]==target:
        l1 = [nums[i], nums[i+1]]
        print(l1)
        break

    elif i+1 > nums.index(x):
        