# list methods

orders=["friedrice","gheeroast","vb","cb","bb","vb","cb","bb","cb"]

# 1. append ->add an element at the end of the list
# orders.append("tea")
# print(orders)

# 2. count() ->occurence of an element in list
# print(orders.count("cb"))

# 3. index() ->position of an element in list
# print(orders.index("gheeroast"))

# 4. pop() ->remove last element from list
# print(orders.pop())#index=-1
# print(orders)
# print(orders.pop(-3))
# print(orders)

# 5. insert(index,object) ->add a new element to specified position
# orders.insert(1,"goby")
# print(orders)

# 6. remove(obj) ->remove the element by giving object
# orders.remove("vb")
# print(orders)

# 7. copy() ->copy the list
mobin_fvt_colors=["red","green","blue","white","yellow","black"]
manoj_fvt_colors=mobin_fvt_colors.copy()
manoj_fvt_colors.remove("yellow")
print(manoj_fvt_colors)
print(mobin_fvt_colors)

# reverse() ->reverse the list
# mobin_fvt_colors.reverse()
# print(mobin_fvt_colors)

# sort()
mobin_fvt_colors.sort()
print(mobin_fvt_colors)
mobin_fvt_colors.sort(reverse=True) #sort in reverse order
print(mobin_fvt_colors)

