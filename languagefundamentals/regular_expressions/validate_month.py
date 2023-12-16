# month 01 - 12

from re import *
month=input("Enter the month in mm:")
rule="(0)[1-9]|(1)[0-2]"   # "(0[1-9]|1[012])"          # |-> or     # (0|1) means 0 or 1
matcher=fullmatch(rule,month)
print("Invalid" if matcher==None else "Valid")
