from re import *

f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\regular_expressions\\vehicle_numbers.txt","r")
rule="(KL|TN)(-)[0-9]{2}(-)[A-Z]{1,2}(-)[0-9]{4}"
for line in f:
    vehicle_number=line.rstrip("\n")
    matcher=fullmatch(rule,vehicle_number)
    if matcher!=None:
        print(vehicle_number)
