# 1. Write a Python program to find the second largest number in a list.

num_lst=[5,7,9,4,8,2]
largest=max(num_lst)
# print(largest)
num_lst.remove(largest)
print(f"Second largest number is {max(num_lst)}")


#     2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.

# Let’s filter out anyone less than 170cm.

height_dict={"john":177,"vijin":165,"hari":173,"roy":175,"tom":169}
for k,v in height_dict.items():
    if height_dict.get(k)<170:
        print(k,v)


# 3. Pattern print 
#                             4 4 4 4 4 4 4  
#                             4 3 3 3 3 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 2 1 2 3 4   
#                             4 3 2 2 2 3 4   
#                             4 3 3 3 3 3 4   
#                             4 4 4 4 4 4 4

num=4
for row in range(1,2*num):
    for col in range(1,2*num):
        print(max(row-3,col-3,2*num-row-3,2*num-col-3), end=" ")
    print()
