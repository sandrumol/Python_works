from re import *

text="fat-cat-run-fast-catch"
pattern="at"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(count)