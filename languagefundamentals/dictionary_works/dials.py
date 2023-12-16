dials={"1":["a","b","c"],
       "2":["d","e","f"],
       "3":["g","h","i"]}
user_input="12"  
# output= (a,d),(a,e),(a,f),(b,d),(b,e),(b,f),(c,d),(c,e),(c,f)
mainlist=[]
for ch in user_input:
    if ch in dials:
       sublst=dials[ch]
       mainlist.append(sublst)
print(mainlist)
