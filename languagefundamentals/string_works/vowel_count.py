# text="pneumonoultramicroscopicsilicovolcanoconiosis"
# vowel_count=0
# for ch in text:
#     if ch in "aeiou":
#         vowel_count+=1
# print(f"Vowel count={vowel_count}")
# print(f"Total number of characters={len(text)}")

#OR

# text="pneumonoultramicroscopicsilicovolcanoconiosis"
# vowel_count=0
# for ch in text:
#     if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
#         vowel_count+=1
# print(f"Vowel count={vowel_count}")
# print(f"Total number of characters={len(text)}")

#OR

text="pneumonoultramicroscopicsilicovolcanoconiosis"
vowel_count=0
for ch in text:
    if ch in ["a","e","i","o","u"]:
        vowel_count+=1
print(f"Vowel count={vowel_count}")
print(f"Consonants count={len(text)-vowel_count}")
print(f"Total number of characters={len(text)}")