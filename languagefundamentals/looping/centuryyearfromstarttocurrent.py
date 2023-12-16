# print all century years from starting year to current year

current_year=2023
starting_year=int(input("Enter the year:"))

# while (starting_year<=current_year):
#     if(starting_year%100==0):
#         print(starting_year)
#     starting_year+=1


# century years using for loop

for starting_year in range(starting_year,current_year):
    if(starting_year%100==0):
        print(starting_year)
    