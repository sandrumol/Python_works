#addition

def add(n1,n2):
    res=n1+n2
    return res
out=add(100,200)
# print(f"Sum={out}")

def add_three(n1,n2,n3):
    res=n1+n2+n3
    print(res)
# add_three(10,20,30)


# cube of a number

def cube(num):
    res=num**3
    return res
# print(cube(4))


#check num is positive or negative
 
def num_check(num):
    res="+ve" if num>0 else "-ve" if num<0 else "zero"
    return res
# print(num_check(5))


# subtraction

def subtract(n1,n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res
# print(subtract(10,20))


# multiplication

def multiply(n1,n2):
    res=n1*n2
    return res
# print(multiply(4,6))


# division

def division(n1,n2):
    res=n1/n2
    return res
# print(division(20,5))


# check odd or even

def odd_even(num):
    res="even" if num%2==0 else "odd"
    return res
# print(odd_even(11))


# cube of a number

def cube():
    num=2
    res=num**3
    return res
# print(cube())

def cube(num=2):# by providing default value of num as 2
    res=num**3
    return res
# print(cube())


# find nth power of num

def nth_power(num,n):
    res=num**n
    return res
# print(nth_power(5,4))

def nth_power(num,n=2):
    res=num**n
    return res
# print(nth_power(5))


# find oneth place smallest number

def oneth_place_small(n1,n2):
    rem1=n1%10
    rem2=n2%10
    res=n1 if rem1<rem2 else n2
    return res
# print(oneth_place_small(432,18))


# century year

def is_century_year(year):
    res=True if year%100==0 else False
    return res
# print(is_century_year(2000))
# print(is_century_year(2023))


# is_leap_year

def is_leap_year(year):
    res=True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False
    return res
# print(is_leap_year(2006))
# print(is_leap_year(2000))


# factorial(num)

def factorial(num=0):
    fact=1
    while(num!=0):
        fact=fact*num
        num=num-1
    return fact
# print(factorial(5))

#OR

def factorial(num=0):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
# print(factorial(5))

# is_prime(num)

def is_prime(num):
    res=True
    for i in range(2,num):
        if num%i==0:
            res=False
            break
    return res
# print(is_prime(13))
# print(is_prime(12))


# is_armstrong(num)

def is_armstrong(num):
    original_num=num
    n=str(num)
    length=len(n)
    sum=0
    while(num!=0):
        digit=num%10
        sum=sum+digit**length
        num=num//10
    res=True if sum==original_num else False
    return res
# print(is_armstrong(153))
# print(is_armstrong(160))
# print(is_armstrong(1634))



