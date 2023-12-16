from re import *

f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\regular_expressions\\numbers.txt","r")

rule="([+]91)?[1-9]{1}[0-9]{9}"
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
        print(number)

