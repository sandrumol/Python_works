# 1. Write a Python program to find n natural number in ascending order

num=int(input("Enter the limit:"))
lst_asc=[i for i in range(1,num+1)]
print(lst_asc)


# 2.Write a python program to find n natural number in descending order

num=int(input("Enter the limit:"))
lst_desc=[i for i in range(num,0,-1)]
print(lst_desc)


# 3.Pattern print 
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

for row in range(5,0,-1):
    for space in range(1,row+1):
        print(" ",end="")
    for col in range(space,6):
        print("*",end="")
    print()

