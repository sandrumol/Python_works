text="ABCABBDE"
# print non repeating characters   
words={}
for ch in text:
    if ch in words:
        words[ch]+=1
    else:
        words[ch]=1

for ch in words:        
    if words[ch]==1:
        print(ch)

# OR

# for k,v in words.items():
#     if v==1:
#         print(k)
