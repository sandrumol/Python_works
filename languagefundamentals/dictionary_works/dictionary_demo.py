student={"name":"sandra","class":"python","roll no":57,"total":60,"location":"pampakuda"}
# print(student)
# print(student["name"])
# print(student["roll no"])


product={"id":1001,"name":"orange","price":35}


# keys()-> return all keys in dictionary
# for k in product.keys():
#     print(k)

# values()-> return all values in a dictionary
# for v in product.values():
#     print(v)

# items()-> return both keys and values in a dictionary
for k,v in product.items():
    print(k,v)

# get(key)-> return a specific value using a key from dictionary, it returns None when the given key is not in dictionary
# print(product.get("price"))
# print(product.get("prices"))
# print("here")

product["price"]=50     # update the value of a key
print(product)

# update({key:value})-> update the value in a dictionary
product.update({"name":"oranges"})
print(product)

# pop(key)-> remove element from a dictionary
product.pop("price")
print(product)

# add offer to the product
# product["offer"]=10
# print(product)

# OR
product.update({"offer":10})
print(product)

# check color in product
print("color" in product) #False

