# kerala vehicle numbers 
# start with kl
# followed by 2 digits
# followed by 1 or 2 alphabets
# followed by 4 digits

from re import *

vehicle_number=input("Enter vehicle number:")

rule="(KL)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"  # (-)? means - is optional

matcher=fullmatch(rule,vehicle_number)
print("Invalid" if matcher==None else "Valid")
