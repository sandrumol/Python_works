# indian mobile number
# +91 1234-456789
# first Exit code – 00 (+)
# followed by indian country code – 91


from re import *

indian_mobile_no=input("Enter the mobile number:")
rule="([+]91 )?[1-9]{4}(-)?[0-9]{6}"
matcher=fullmatch(rule,indian_mobile_no)
print("Invalid" if matcher==None else "Valid")
