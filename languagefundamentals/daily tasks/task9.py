# 1. Write a Python program to find leap year (user input)

year=int(input("Enter the year:"))
if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# 2.Write a python program to sum all the items in the dictionary 

number_dict={"one":1,"five":5,"six":6,"ten":10,"twenty":20}
sum=0
for v in number_dict:
    sum+=number_dict[v]
print(f"Sum={sum}") #42


# 3.Pattern print 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *

for row in range(1,6):
    for col in range(1,6):
        print("*",end=" ")
    print()

