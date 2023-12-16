# list comprehension

# [return value  for num in lst  condition]

lst=[2,4,5,6,7,8,9]

# squares=[]
# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)

#OR

squares=[num**2 for num in lst]
# print(squares)

cubes=[num**3 for num in lst]
# print(cubes)

num_gt_five=[num for num in lst if num>5]
# print(num_gt_five)

odd=[num for num in lst if num%2!=0]
# print(odd)

c4=["manoj","bilal","akash","malavika","jamina","akshay"]
names_upper=[names.upper() for names in c4]
# print(names_upper)

names_gt_five=[names for names in c4 if len(names)>5]
# print(names_gt_five)


# evens=[]
# for num in lst:
#     if num%2==0:
#         evens.append(num)
# print(evens)

#OR

evens=[num for num in lst if num%2==0]
# print(evens)



lst=["Red","green","blue","white","black","Apple","ignore","under"]

#print words start with vowels


# for i in range(0,len(lst)):
#     if lst[i].startswith("a") or lst[i].startswith("e") or lst[i].startswith("i") or lst[i].startswith("o") or lst[i].startswith("u"):
#         print(lst[i])
# vowels=[words for words in lst if words.startswith("a") or words.startswith("e") or words.startswith("i") or words.startswith("o") or words.startswith("u")]
# print(vowels)

# OR

# vowels=[words for words in lst if words.startswith(("a","e","i","o","u"))]
# print(vowels)

#  OR

vowels=[words for words in lst if words[0].lower() in ["a","e","i","o","u"]]
print(vowels)



#print words start with consonants


# for i in range(0,len(lst)):
#     if lst[i].startswith("a") or lst[i].startswith("e") or lst[i].startswith("i") or lst[i].startswith("o") or lst[i].startswith("u"):
#         break
#     else:
#         print(lst[i])

# OR

# consonants=[words for words in lst if not words.startswith(("a","e","i","o","u"))]
# print(consonants)

# OR

consonants=[words for words in lst if words[0].lower() not in ["a","e","i","o","u"]]
print(consonants)


