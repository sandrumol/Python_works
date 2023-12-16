
from re import *

text="ab CaK2@#"

# pattern="\d" # returns numbers [0-9]
# pattern="\D" # returns characters excluding digits [^0-9]
# pattern="\w"  # returns alphanumeric characters [a-zA-Z0-9]
pattern="\W"  # returns all characters except alphanumeric characters [^a-zA-Z0-9]

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())