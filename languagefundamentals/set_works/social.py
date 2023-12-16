insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}

mohanlal_followings={"prithvi","vijay","lalu"}

mohanlal_suggestions=insta_users.difference(mohanlal_followings)
mohanlal_suggestions.discard("mohanlal")
print(mohanlal_suggestions)

dq_friends={"prithvi","fahad","lalu","sureshgopi"}
mutual_friends_dq_mohanlal=mohanlal_followings.intersection(dq_friends)
print(mutual_friends_dq_mohanlal)



# symmetric difference
#  (A U B) – (A ∩ B)
order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"}
order_union=order1.union(order2)
order_inter=order1.intersection(order2)
print(order_union)
print(order_inter)
order=order_union.difference(order_inter)
# OR
# order=order_union-order_inter 
# print(order)

# OR
order=order1.symmetric_difference(order2)
print(order)