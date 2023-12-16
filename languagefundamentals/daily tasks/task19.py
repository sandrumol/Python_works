# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers

num_lst=[1,-2,3,-4,5,6,7,-8,-9,10]
triplet_lst=[]
c=0
for i in num_lst:
    for j in num_lst:
        t=-(i+j)
        if t in num_lst:
            temp_lst=[i,j,t]
            temp_lst.sort()
            if temp_lst not in triplet_lst:
                triplet_lst.append(temp_lst)
print(f"The triplets whose sum is zero={triplet_lst}")


#     2. Write a python program to make combinations of 3 digits

number_lst=[2,1,7,3]
number_set=set()
for i in number_lst:
    for j in number_lst:
        for k in number_lst:
            if i!=j and i!=k and j!=k:
                number=i*100+j*10+k
                number_set.add(number)
print(number_set)


# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

for row in range(1,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        if col in [1,row]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for row in range(5,1,-1):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row):
        if col in [1,row-1]:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()