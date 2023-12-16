from re import *

variable_name=input("Enter the variable name:")


rule="[a-zA-Z]{1}[a-zA-Z0-9_]*"

matcher=fullmatch(rule,variable_name)  # fullmatch checks the entire pattern match with rule
print("Invalid" if matcher==None else "Valid")