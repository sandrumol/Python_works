his_age=int(input("Enter his_age:"))
her_age=int(input("Enter her_age:"))
married_status=int(input("Select status press 1 for married, 2 for single:"))
if his_age>=21 and her_age>=18 and married_status==2:
    print("Proceed")
else:
    print("not possible")