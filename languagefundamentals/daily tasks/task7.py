# 1. Write a Python program that separate positive and negative numbers from a list

lst=[1,4,-3,5,-7,2,3,-8,-9]
positive_lst=[]
negative_lst=[]
for i in range(0,len(lst)):
    if lst[i]>0:
        positive_lst.append(lst[i])
    elif lst[i]<0:
        negative_lst.append(lst[i])
print(f"Postive numbers list={positive_lst}")
print(f"Negative numbers list={negative_lst}")


# 2.Write a python program to reverse the tuple

tp=(10,40,20,50,30,90)
tp_reverse=[]
for i in range(len(tp)-1,-1,-1):
    tp_reverse.append(tp[i])
tp_reverse=tuple(tp_reverse)
print(tp_reverse)


# 3.Pattern print
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3 
# 4 4  
# 5

for row in range(1,6):
    for col in range(row,6):
        print(row,end=" ")
    print()

