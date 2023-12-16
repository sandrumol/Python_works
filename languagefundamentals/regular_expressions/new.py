from re import *

variable_name=input("Enter the variable name:")
# starting with k,l,m,n
# second place must be a digit and that is divisible by 3
# followed by any number of alphabets and digits

rule="[klmnKLMN]{1}[369]{1}[a-zA-Z0-9]*"  # OR "[k-nK-N][a-zA-Z0-9]*"

matcher=fullmatch(rule,variable_name)

print("Invalid" if matcher==None else "Valid")
