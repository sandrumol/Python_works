colors=["red","green","blue","white","red","white"]
# print(colors) # insertion order is preserved, duplicate allowed
# print(colors[2])

colors[1]="purple"
# print(colors) # list can be updated

colours=["red","green","blue",12,True,12.5]
# print(colours)



expenses=[12000,13000,23000,24000,25000,32000,23000]

# for i in range(0,6):
#     print(expenses[i])

#OR

# for exp in expenses:
#     print(exp)



# print all expenses > 20000

# for exp in expenses:
#     if exp>20000:
#         print(exp)

# OR

# for i in range(0,len(expenses)):
#     if expenses[i]>20000:
#         print(expenses[i])



# print all expenses in range of 15K-25k

# for i in range(0,len(expenses)):
    # if expenses[i]>15000 and expenses[i]<25000:
    #     print(expenses[i])

#OR

# for i in range(0,len(expenses)):
#     if expenses[i] in range(15000,25000):
#         print(expenses[i])



# print maximum expense

# srt=sorted(expenses,reverse=True)
# print(srt)
# print(srt[0])

#OR

# max_exp=max(expenses)
# print(f"Maximum expense={max_exp}")

# #minimum expense

# min_exp=min(expenses)
# print(f"Minimum expense={min_exp}")

# # total_expenses

# total_exp=sum(expenses)
# print(f"Total expense={total_exp}")

# # average_expenses

# avg_exp=total_exp/len(expenses)
# print(f"Average expense={avg_exp}")



items=["bat","ball","stumps","helmet","arc","cricketball"]

# find longest word

def get_len(w):
    return len(w)
# longest_word=max(items,key=lambda w:len(w))
# OR 
longest_word=max(items,key=get_len)
# print(f"Longest word={longest_word}")


# smallest word

smallest_word=min(items,key=lambda w:len(w))
# print(f"Smallest word={smallest_word}")



# print sum of characters in items[]

sum=0
for i in range(0,len(items)):
    length=len(items[i])
    sum=sum+length
print(f"Total characters={sum}")



# find longest_word from given list without using built in functions

# for i in range(0,len(items)):
#     if len(items[i-1])<len(items[i]):
#         c=items[i]
# print(c)

#OR

max_item=items[0]
for i in range(1,len(items)):
    current_item=items[i]
    if len(current_item)>len(max_item):
        max_item=current_item
print(max_item)



#  find smallest_word from given list without using built in functions

min_item=items[0]
for i in range(1,len(items)):
    current_item=items[i]
    if len(current_item)<len(min_item):
        min_item=current_item
print(min_item)












lst=[5,6,2,7,3,1,5]
# lst[start:stop:step]

print(lst[-3:-1])  #[3,1]
