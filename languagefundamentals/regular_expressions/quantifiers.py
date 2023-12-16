from re import *

text="aaabcaabbaaaabd"
count=0

# pattern="a*"  # any number of 'a' including not 'a' condition             [a-z]*   [0-9]*/
# pattern="a{2}" # 'aa' condition
pattern="a{2,4}"  # minimum match of 'a' is 2 and maximamu is 4             [0-9]{1,2}

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)