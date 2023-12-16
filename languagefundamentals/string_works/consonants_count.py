text="#@12pneumonoultramicroscopicsilicovolcanoconiosis"

con_count=0
for ch in text:
    if ch not in ["a","e","i","o","u"] and ch.isalpha():
        con_count+=1
print(f"Consonants count={con_count}")
print(f"Total number of characters={len(text)}")

