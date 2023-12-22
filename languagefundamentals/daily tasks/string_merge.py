# string merge

string1=input("Enter the first string:") # "ABC"
string2=input("Enter the second string:") # "PQRST"
smallest_length=min(len(string1),len(string2))
result=""
for i in range(0,smallest_length):
    result=result+string1[i]+string2[i]
# print(result)
if len(string1)>len(string2):
    rem=string1[smallest_length:]
else:
    rem=string2[smallest_length:]
result+=rem
print(result)


# -------------------------------------------------------------------------------------


# list merge

# ["a","b","c"]
# ["d","e","f","g","h"]
# "adbecfgh"

lst1=["a","b","c"]
lst2=["d","e","f","g","h"]
smallest_length=min(len(lst1),len(lst2))
output=""
for i in range(0,smallest_length):
    output=output+lst1[i]+lst2[i] 
# print(output)
# j=len(lst1)   
# while(len(lst2)>j):
#     output=output+lst2[j]
#     j+=1

if len(lst1)>len(lst2):
    rem=lst1[smallest_length:]
    rem_str="".join(rem)
else:
    rem=lst2[smallest_length:]
    rem_str="".join(rem)
    # print(rem_str)
output+=rem_str
print(output)