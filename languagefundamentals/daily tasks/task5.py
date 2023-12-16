# 1.Write a python program to find factorial of a prime number

num=int(input("Enter the number:"))
fact=1
is_prime=True
for i in range(2,num):
    if num%i==0:
        is_prime=False
        print("Not a prime number")
        break
if is_prime==True:
    original_num=num
    while(num>=1): 
        fact=fact*num
        num=num-1
    print(f"Factorial of {original_num} is {fact}")


# 2.Write a python program to display Fibonacci series and specify that number odd or even

num=int(input("Enter the limit:")) # 5
prev=0
current=1
print(prev,"Even")
print(current,"Odd")
for i in range(0,num-2):
    next=prev+current
    result="Even" if next%2==0 else "Odd"
    print(next,result)
    prev=current
    current=next


# 3.Write a python program to reverse digits in a number

num=int(input("Enter the number:")) 
while(num!=0):
    digit=num%10
    print(digit,end="")
    num=num//10

