# print train numbers

from re import *
f= open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\regular_expressions\\news.txt","r")
rule="[0-9]{5}"
# for line in f:
#     lst=line.rstrip("\n").split(" ")
#     # print(lst)
#     for train_number in lst:
#         matcher=fullmatch(rule,train_number)
#         if matcher!=None:
#             print(train_number)

# OR

for line in f:
    words=line.rstrip("\n")
    matcher=finditer(rule,words)
    for m in matcher:
        print(m.group())
