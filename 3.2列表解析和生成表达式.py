
nums = []
for i in range(1,10):
    if  i%3==0 or i%5==0:
        nums.append(i)
print(nums)
print(sum(nums))

nums1 = [j for j in range(1,1000) if j%3==0 or j%5==0]


print(nums1)
print(sum(nums1))
