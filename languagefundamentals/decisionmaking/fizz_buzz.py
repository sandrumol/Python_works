# fizz buzz program
# print fizz if num divisible by 3, print buzz if num divisible by 5,print fizzbuzz if num divisible by 15

num=int(input("Enter the number:"))
if num%3==0  and num%5!=0:
    print("fizz")
elif num%5==0 and num%3!=0:
    print("buzz")
elif num%5==0 and num%3==0:
    print("fizzbuzz")

# if num%15==0:
#     print("fizzbuzz")
# elif num%5==0:
#     print("buzz")
# elif num%3==0:
#     print("fizz")
# else:
#     print("======")