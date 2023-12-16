# date dd-mm-yy
# year 1900-2099

from re import*
date=input("Enter the date in dd-mm-yyyy:")
rule="(0[1-9]|[12][0-9]|3[01])(-)(0[1-9]|1[0-2])(-)(19|20)[0-9]{2}"
matcher=fullmatch(rule,date)
print("Invalid" if matcher==None else "Valid")

