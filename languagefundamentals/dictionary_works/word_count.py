text="hello hai hello hai"
# word count hello=2,hai=2

lst=text.split(" ")
print(lst)
word={}
for ch in lst:
    if ch in word:
        word[ch]+=1
    else:
        word[ch]=1
print(word)
