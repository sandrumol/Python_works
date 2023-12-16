text="pneumonoultramicroscopicsilicovolcanoconiosis"
# most frequent letter
character={}
for ch in text:
    if ch in character:
        character[ch]+=1
    else:
        character[ch]=1
print(character)
print(max(character,key=lambda k:character.get(k)))