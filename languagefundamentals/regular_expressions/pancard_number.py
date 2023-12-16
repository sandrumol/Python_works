# validate pan card number
# first 3 positions contains alphabets
# 4th position contains p,c,a,f,h,t
# 5th position contain the first letter of pan card holder name
# next 4 position contain numbers
# and last position contain 1 alphabet

from re import *

pancard_number=input("Enter the pan card number:")
name=input("Enter the name:")
first_letter=name[0].upper()
rule="[A-Z]{3}[PCAFHT]{1}"+first_letter+"[0-9]{4}[A-Z]{1}"
matcher=fullmatch(rule,pancard_number)
print("Invalid" if matcher==None else "Valid")

