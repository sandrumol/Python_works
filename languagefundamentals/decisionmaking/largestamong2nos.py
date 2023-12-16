#program to print largest among 2 nos

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
# if num1>num2:
#     print(f"{num1} is the largest")
# elif num2>num1:
#     print(f"{num2} is the largest")
# else:
#     print("Both numbers are equal")

# OR

print(num1 if num1>num2 else num2)