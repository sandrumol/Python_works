# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

original_lst=[1, 3, 5, 1, 3, 2, 5, 4, 2]
new_lst=[]
final_lst=[]
position=0
for i in original_lst:
    if original_lst.count(i)==2:
        new_lst.append(list())
        new_lst[position].append(i)
        new_lst[position].append(i)
        position+=1
    elif original_lst.count(i)==1:
        new_lst.append(list())
        new_lst[position].append(i)
        position+=1
for i in new_lst:
    if i not in final_lst:
        final_lst.append(i)
final_lst=sorted(final_lst)
print(final_lst)


#   2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000

unit=int(input("Enter the unit:"))
amount=0
if unit<=100:
    print("No charge")
elif unit>100:
    amount=amount+5*unit
    if unit>=200:
        next_unit=unit-200
        amount=amount+next_unit*10
print(f"Total bill amount is Rs {amount}")


#        3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E

ascii_code=65 # A
for row in range(1,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(0,row):
        print(chr(ascii_code+col),end=" ")
    print()
