mobile={"id":100,"name":"iphone15","price":100000,"imei":2345,"processor":"apple"}

# print all key value pairs
for k,v in mobile.items():
    print(k,v)

# print name
print(mobile.get("name"))

# print price
print(mobile.get("price"))

# update price as 85000
mobile.update({"price":85000})
print(mobile)

# remove imei
mobile.pop("imei")
print(mobile)

# add offer to the mobile
# mobile["offer"]=1000
# print(mobile)

# OR
mobile.update({"offer":1000})
print(mobile)

# add 1000 to price
mobile["price"]+=1000
print(mobile)

# check color in mobile
print("color" in mobile)

