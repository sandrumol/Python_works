text="ABCABBDDE"
# print second recursive character   output=B
dup_char=[]     # insertion order 
words={}
for ch in text:
    if ch in words:
        words[ch]+=1
        if ch not in dup_char:
            dup_char.append(ch)
    else:
        words[ch]=1
print(words)
print(dup_char)
print(f"second recursive character is {dup_char[1]}")
