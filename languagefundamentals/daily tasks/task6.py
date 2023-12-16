# 1. Write a Python program that accepts a string and calculates the number of digits and letters.

text=input("Enter the string:")
digit_count=0
alpha_count=0
for w in text:
    if w.isdigit()==True:
        digit_count+=1
    elif w.isalpha()==True:
        alpha_count+=1
print(f"Number of digits={digit_count}")
print(f"Number of letters={alpha_count}")


# 2.Write a python program to display multiplication table of a number (user input)

num=int(input("Enter the number:"))
for i in range(1,11):
    print(f"{num}*{i}={i*num}")


# 3.Pattern print
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for row in range(1,6):
    for col in range(0,row):
        print(row,end=" ")
    print()

