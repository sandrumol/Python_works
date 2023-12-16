# program to find gcd of two numbers =>hcf
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
smallest_num=n1 if n1<n2 else n2
fact=1

i=1
while(i<=smallest_num):
    if(n1%i==0 and n2%i==0):
        fact=i
    i+=1
print(f"gcd of {n1} and {n2} is {fact}")
