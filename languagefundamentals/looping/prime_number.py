# check number is prime or not

num=int(input("Enter the number:"))
is_prime=True#number is prime

for i in range(2,num):
    if num%i==0:
        is_prime=False#not a prime number
        break
print(is_prime)