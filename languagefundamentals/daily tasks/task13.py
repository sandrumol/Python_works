# 1. Write a Python program that Use while loop to display elements from a given list present at odd index positions

lst=[20,40,33,12,45,55,75,24,87,7]
length=len(lst)
position=length-1
while(position!=0):
    if position%2!=0:
        print(f"The element at index {position} is {lst[position]}")
    position-=1


# 2.Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

square_lst=[]
cube_lst=[]
for num in range(0,10):
    user_input=int(input("Enter the number:"))
    square=user_input**2
    cube=user_input**3
    square_lst.append(square)
    cube_lst.append(cube)
print(f"Square list={square_lst}")
print(f"Cube list={cube_lst}")


# 3.Pattern print 
# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1

for row in range(1,6):
    for col1 in range(1,row+1):
        print(col1,end=" ")
    for col2 in range(col1-1,0,-1):
        print(col2,end=" ")
    print()
