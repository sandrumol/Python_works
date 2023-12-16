tp=(10,20,30,40)
print(tp)
print(type(tp)) # tuple

tp=(10,20,30,40,20)
print(tp) #duplicate allowed

# tp[0]=100
# print(tp)  #cannot be updated

color=("red")
print(type(color)) #str
colors=("red",)
print(type(colors)) #tuple

# count()
print(tp.count(20))

# index
print(tp.index(40))