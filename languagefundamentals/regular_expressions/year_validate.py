# year 1900-2099

from re import *
year=input("Enter the year in yyyy:")
rule="(19|20)[0-9]{2}"     # or "(19[0-9]{2}|20[0-9]{2})"
matcher=fullmatch(rule,year)
print("Invalid" if matcher==None else "Valid")
