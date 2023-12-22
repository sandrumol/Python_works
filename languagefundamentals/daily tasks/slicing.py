# slicing concept

# [start:stop:step]

#   -(987654321)
name="TECHNOLAB"
#     012345678

# print(name[1]) # E
# print(name[2:4]) # CH
# print(name[:7]) # TECHNOL
# print(name[2:]) # CHNOLAB
# print(name[6:]) # LAB


# negative indexing

# print(name[-1:-4:-1]) # BAL
# print(name[:-5:-1]) # BALO


#string reversal

# reversed_string=name[::-1]
# print(reversed_string)


# palindrome

# word="madam"
# reversed_string=word[::-1]
# print("Palindrome" if word==reversed_string else "Not palindrome")




string1="hai"
string2="goodmorning"
str1_length=len(string1)
rem_string2=string2[str1_length:]
print(rem_string2)


