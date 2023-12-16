# TOPIC = IF STATEMENT

# 1.Write a program to display ‘’HELLO’’ if a number entered by user is a multiple of five, otherwise print ‘’Bye’’.
# number=int(input("Enter a number:"))
# print("HELLO" if number%5==0 else "Bye")


# 2.Write a program to check whether a person is eligible for voting or not
# age=int(input("Enter the age:"))
# print("Eligible for voting" if age>=18 else "Not eligible for voting")


# 3.Write a program to accept percentage from the user and display the grade according to the following criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade
mark=int(input("Enter the percentage:"))
if mark>90:
    print("A Grade")
elif mark>80 and mark<=90:
    print("B Grade")
elif mark>=60 and mark<=80:
    print("C Grade")
elif mark<60:
    print("D Grade")


# 4.Write a program to find the largest number out of three numbers excepted from user.
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# num3=int(input("Enter the third number:"))
# if num1>num2 and num1>num3:
#     print(f"{num1} is largest")
# elif num2>num1 and num2>num3:
#     print(f"{num2} is largest")
# elif num3>num1 and num3>num2:
#     print(f"{num3} is largest")
# else:
#     print("All 3 numbers are equal")
