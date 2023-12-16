# 1. Write a python program to find the sum of elements in a tuple

tp=(2,4,5,7,1,6)
print(f"Sum={sum(tp)}")


# 2.Convert tuple to a list and find sum

tp=(5,3,8,2,4,1)
num_list=list(tp)
print(num_list)
print(f"Sum={sum(num_list)}")


# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E

ascii_code=65 # A
for row in range(1,6):
    for col in range(1,row+1):
        print(chr(ascii_code),end=" ")
    ascii_code+=1
    print()
