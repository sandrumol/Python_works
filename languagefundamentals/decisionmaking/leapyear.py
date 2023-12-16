# to print leap year or not

# to check century year is a leap year => year%100==0 and year%400==0
# to check non century year is a leap year => year%100!=0 and year%4==0

year=int(input("Enter the year:"))
if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# OR
# if year%400==0 or year%100!=0 and year%4==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")