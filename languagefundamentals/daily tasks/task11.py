# 1. Write a Python program that print 2 list and common element

lst1=[3,4,2,7,1,8,4]
lst2=[9,1,5,0,7,3,6]
common_element_lst=[]
for num in lst1:
    if num in lst2:
        common_element_lst.append(num)
print(lst1)
print(lst2)
print(common_element_lst)


# 2.Write a python program to find the least square number from a list

lst=[5,8,24,16,30,49,60]
square_lst=[]
for num in lst:
    sq_root=int(num**0.5)
    print(sq_root)
    square_lst.append(sq_root**2)
sort_lst=sorted(lst)
# print(sort_lst)
# print(square_lst)
for n in lst:
    if n in square_lst:
        print(f"Least square number={n}")
        break


# 3.Pattern print 
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

