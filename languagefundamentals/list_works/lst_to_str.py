nums=[12,67,5,8]

# str_nums=[]
# for n in nums:
#     str_nums.append(str(n))
# print(str_nums)

# OR

str_nums=[str(n) for n in nums]
print(str_nums) # lst to str
str_nums.sort(reverse=True)
print(str_nums)  #['8', '67', '5', '12']
for i in range(0,len(str_nums)):
    print(str_nums[i],end="")