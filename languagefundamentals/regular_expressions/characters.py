# find a or c in given string

from re import *
text="kaBczabc 9@7c"

# pattern="[a-zA-Z0-9]"  # "[ac]" means a or c
# pattern="[^a-z]"   # excluding lowercase letters and return other characters
# pattern="[a-e]"    # means match from a to e that is "[abcde]"="[a-e]"
# pattern="[a-z]"    # means lower case a to z
# pattern="[A-Z]"    # means upper case A to Z
# pattern="[a-zA-Z]" # matches all alphabtes
# pattern="[0-9]"    # matches all digits
# pattern="[a-zA-Z0-9]" # matches alphanumeric characters
pattern="[^a-zA-Z0-9]" # returns other characters except alphanumeric characters

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

