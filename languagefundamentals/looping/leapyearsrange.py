# print all non leap years from starting year to current year

current_year=2023
starting_year=int(input("Enter the year:"))

# while (starting_year<=current_year):
#     if(starting_year%100==0 and starting_year%400==0 or starting_year%100!=0 and starting_year%4==0):
#         print(starting_year)
#     starting_year+=1


# leap years 1800 to 2024 using for loop

for year in range(starting_year,current_year):
    if(year%100==0 and year%400==0 or year%100!=0 and year%4==0):
        print(year)