# 1. Write a Python program that keep on accepting number from the user until users enter zero display the sum of all number

# user_input=int(input("Enter the number:"))
sum=0
while(user_input!=0):
    sum+=user_input
    user_input=int(input("Enter the number:"))
print(f"Sum={sum}")


# 2.Write a python program to accept decimal number and display it’s binary number

num=int(input("Enter the number:"))
original_num=num
binary=""
if num==0:
    binary=0
else:
    while num>0:
        digit=num%2
        # print(digit)
        binary=str(digit)+binary
        # print(binary)
        num=num//2
        # print(num)
print(f"The binary of {original_num} is {binary}")


# 3.Pattern print 
# 6 6 6 6 6 6 
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

for row in range(6,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()










# decimal to binary==>

#  num=5   -> digit=5%2=1 binary=1   num=5//2=2
            # digit=2%2=0 binary=01  num=2//2=1
            # digit=1%2=1 binary=101  num=1//2=0
    

