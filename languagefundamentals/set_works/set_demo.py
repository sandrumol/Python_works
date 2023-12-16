st={10,20,30}
print(st)
print(type(st)) #set
st={}
print(type(st)) #dict
empty_set=set()

st={20,10,True,30,"hello"}
print(st) #insertion order is not preserved 
# print(st[0]) #indexing not supported

st={20,10,True,30,"hello",10,20}
print(st) #duplicates not allowed all elements are unique


colors={"red","green","blue"}

# add()-> add new element in set
colors.add("yellow")
print(colors)

# intersection()-> common elements from two sets
st1={"red","green","blue"}
st2={"purple","yellow","cyan","blue"}
inter_set=st1.intersection(st2)
print(inter_set)

# union()-> return all unique elements from two sets 
union_set=st1.union(st2)
print(union_set)

# difference()-> remove set2 elements from set1 (diff=st1.difference(st2))
diff_set=st1.difference(st2)
print(diff_set)

# pop()-> remove element from set
st1.pop()
print(st1)

# remove(obj)-> remove the specified element from set
st2.remove("yellow")
print(st2)

# discard()-> remove the specified element from set, if element is not in set it will not display any error
st2.discard("blue")
print(st2)
st2.discard("reds")
print("here") #here will print

# symmetric_difference()-> (A U B) – (A ∩ B)
order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"}
order=order1.symmetric_difference(order2)
print(order)

# update()-> a set can update by using another set
st1={10,20,30}
st2={100,200,300}
st1.update(st2)
print(st1)