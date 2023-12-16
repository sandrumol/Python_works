text="ABCABBDE"
# print first recursive character   output=A
words={}
for ch in text:
    if ch in words:
        print(f"first recursive character is {ch}")
        break
    else:
        words[ch]=1
