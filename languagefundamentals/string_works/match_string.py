#Anagram program

# source_word="won"
# target_word="now"
# ch=""
# if ch in source_word:
#     print("True" if ch in target_word else "False")

#OR

source_word="won"
target_word="now"
srt_source=sorted(source_word)
srt_target=sorted(target_word)
print("True" if srt_source==srt_target else "False")