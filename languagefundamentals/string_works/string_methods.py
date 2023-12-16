# in case of method calling and function calling we have to use () after name

company="LUMINAR"

print(company.casefold()) #uppercase to lowercase           luminar

print()

print(company.capitalize())  #                              Luminar

print()

print(company.lower()) #lowercase                           luminar

print()

name="luminar"
print(name.upper()) # uppercase                             LUMINAR

print()

word="2car"
print(word.isalpha()) # returns either True or False        False
print(name.isalpha()) #                                     True

print("----------")

number="123"
print(word.isdigit()) # returns either True or False        False
print(number.isdigit()) #                                   True

print("----------")

special="ab@#$344"
print(word.isalnum()) # returns either True or False        True
print(name.isalnum())#                                      True
print(number.isalnum())#                                    True
print(special.isalnum())#                                   False

print("----------")

word1="\nhello\n"
print(word1.strip("\n")) # strip("char") remove the char from given word

print()

word1="hello\n"
print(word1.lstrip("\n")) #remove the char on left side from given word

print()

word1="\nhello"
print(word1.rstrip("\n")) #remove the char on right side from given word

print()

word="hello world"
print(word.split()) #split a sentence or string to list

print()

text="pneumonoultramicroscopicsilicovolcanoconiosis"
print(text.startswith("pn")) #returns True if string starts with pn else false
print(text.startswith("mo")) #False

print("----------")

print(text.endswith("sis")) #returns True if string ends with sis else false
print(text.endswith("pne")) #False

print()

print(text.count("o")) #returns the number of a character in a string
print(text.count("n"))

print("----------")

print(text.index("p")) #to specify the index position of character in a string , index starts from 0
print(text.index("e"))
print(text.index("sis"))

print()

text="hello"
out=",".join(text)
print(out) #h,e,l,l,o