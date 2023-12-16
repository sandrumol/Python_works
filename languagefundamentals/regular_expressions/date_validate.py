# date 01-31

from re import *

date=input("Enter the date in dd:")
rule="(0[1-9]|[12][0-9]|3[01])"   # or  "(0[1-9]|1[0-9]|2[0-9]|3[01])"
matcher=fullmatch(rule,date)
print("Invalid" if matcher==None else "Valid")
