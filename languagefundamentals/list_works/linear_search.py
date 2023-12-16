# linear search => more complex

lst=[10,2,11,5,7,20]
element=int(input("Enter element:"))
# i=0
# is_present=False
# while(i<len(lst)):
#     cur_element=lst[i]
#     if cur_element==element:
#         is_present=True
#         break
#     i+=1
# print(is_present)


is_present=False
for i in range(0,len(lst)):
    cur_element=lst[i]
    if cur_element==element:
        is_present=True
        break
print(is_present)