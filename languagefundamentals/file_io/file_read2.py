
f=open("C:\\Users\\SANDRA SKARIA\\OneDrive\\Desktop\\Python Works\\languagefundamentals\\file_io\\news.txt","r")

# total number of words

# count=0
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     print(words)
#     count+=len(words)
# print(f"Total number of words={count}")



# word count of each word

word_count={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in word_count:
            word_count[w]+=1
        else:
            word_count[w]=1
print(word_count)