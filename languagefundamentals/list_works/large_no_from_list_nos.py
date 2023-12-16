lst=[23,12,3,78,9]
# generate largest number from the numbers in list  output=9782312
# lst.sort()

# for i in range(0,len(lst)):
#     if lst[i]<10:
#         one_digit_no=lst[i]
#         print(one_digit_no,end="")
#     rem_lst=sorted(lst,reverse=True)
#     if one_digit_no!=rem_lst[i]:
#         print(rem_lst[i],end="")

srt=sorted(lst,key=lambda num:num//10 if num>10 else num,reverse=True)
for i in range(0,len(srt)):
    print(srt[i],end="")

# OR

str_nums=[str(n) for n in lst]
print(str_nums)
str_nums.sort(reverse=True)
for i in range(0,len(str_nums)):
    print(str_nums[i],end="")