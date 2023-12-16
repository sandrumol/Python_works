# 1. Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3 

for num in range(10,51):
    if num%2!=0 and num%3!=0:
        print(num)


#     2. Python program to check if the given string is a palindrome.

text=input("Enter the string:")
text=text.lower()
rev_text=text[::-1]
# print(rev_text)
if text==rev_text:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")


#        3. Pattern print 
#            1 1 1 1 1 1 1
#            2 2 2 2 2 2 2
#            3 3 3 3 3 3 3 
#            4 4 4 4 4 4 4
#            5 5 5 5 5 5 5

for row in range(1,6):
    for col in range(1,8):
        print(row,end=" ")
    print()
