# us phone number
# +1-650-513-0514  or  001-650-513-0514
# first Exit code – 00 (+)
# followed by US country code – 1
# 3 digit area code
# 7 digit number

from re import *

phone_number=input("Enter the phone number:")
rule="[+](1)-[0-9]{3}-[0-9]{3}-[0-9]{4}"

matcher=fullmatch(rule,phone_number)
print("Invalid" if matcher==None else "Valid")

