# 1.Write a program to accept two numbers and mathematical operators and perform operation accordingly
# Output:
# Enter 1st number :10
# Enter 2nd number:5
# Enter operator: -
# The answer:5

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))
operator=input("Enter operator:")
if operator=="+":
    result=num1+num2
    print(result)
elif operator=="-":
    result=num1-num2
    print(result)
elif operator=="*":
    result=num1*num2
    print(result)
elif operator=="/":
    result=num1/num2
    print(result)
elif operator=="//":
    result=num1//num2
    print(result)
elif operator=="%":
    result=num1%num2
    print(result)


# 2. Take input of age of 3 people by user and determine oldest and youngest among them.

age1=int(input("Enter the age of 1st person:"))
age2=int(input("Enter the age of 2nd person:"))
age3=int(input("Enter the age of 3rd person:"))
if age1>age2>age3:
    print(f"The oldest is {age1} years")
    print(f"The youngest is {age3} years")
elif age1>age3>age2:
    print(f"The oldest is {age1} years")
    print(f"The youngest is {age2} years")
elif age2>age1>age3:
    print(f"The oldest is {age2} years")
    print(f"The youngest is {age3} years")
elif age2>age3>age1:
    print(f"The oldest is {age2} years")
    print(f"The youngest is {age1} years")
elif age3>age1>age2:
    print(f"The oldest is {age3} years")
    print(f"The youngest is {age2} years")
elif age3>age2>age1:
    print(f"The oldest is {age3} years")
    print(f"The youngest is {age1} years")


# 3. Take values of length and breadth of a rectangle from user and check if it is square or not.

length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
if length==breadth:
    print("It is a square")
else:
    print("It is a rectangle")
