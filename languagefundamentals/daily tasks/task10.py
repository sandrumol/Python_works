# 1. Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, until the number with in the range that we given

num=int(input("Enter the number:"))
is_correct_num=True
while(is_correct_num==True):
    if num>=10 and num<=50:
        print(f"{num} is a correct number")
        break
    else:
        num=int(input("Enter the correct number:"))
        

# 2.Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list

start=int(input("Enter the first number:"))
end=int(input("Enter the last number:"))
lst=[]
for i in range(start,end+1):
    if i%2==0: #and i%5!=0:
        lst.append(i)
print(f"Even numbers list={lst}")
# final_lst=[i for i in lst if i%5!=0]
# print(final_lst)
for i in lst:
    if i%5==0:
        lst.remove(i)
print(lst)


# 3.Pattern print 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *


for row in range(1,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end=" ")
    print()
for row in range(6,1,-1):
    for space in range(6,row,-1):
        print(" ",end="")
    for col in range(1,row):
        print("*",end=" ")
    print()

