# program to print century year or not

year=int(input("Enter the year:"))
if year%100==0:
    print(f"{year} is a century year")
else:
    print(f"{year} is not a century year")