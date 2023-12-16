#Kangroo words => target word can form from a source word
#program to check kangroo words or not

source_word="chicken"#savage
target_word="checn"#save

src=" ".join(source_word)
target=" ".join(target_word)
flag=1
print(src)
print(target)
for w in src:
    if w in target and flag==1:
        flag=1     
    else:
        flag=0
if flag==1:
    print(f"{target_word} is a kangroo word of {source_word}")
else:
    print(f"{target_word} is not a kangroo word of {source_word}")

# OR

source_word_lst=[ch for ch in source_word]
target_word_lst=[ch for ch in target_word]
print(source_word_lst)
print(target_word_lst)
for ch in target_word_lst:
    if ch in source_word_lst:
        source_word_lst.remove(ch)
    else:
        print(f"{target_word} is not a kangroo word of {source_word}")
        break
else:
    print(f"{target_word} is a kangroo word of {source_word}")