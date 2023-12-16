# 1. Write a python program to create a list of tuples having first element as the number and second element as the cube of the number

start_num=int(input("Enter the first number:"))
end_num=int(input("Enter the last number:"))
tp_num=[]
tp_num_cube=[]
num_lst=[]
for i in range(start_num,end_num+1):
    tp_num.append(i)
    tp_num_cube.append(i**3)
tp_num=tuple(tp_num)
tp_num_cube=tuple(tp_num_cube)
num_lst.append(tp_num)
num_lst.append(tp_num_cube)
print(num_lst)


# 2. find the length of the string using for loop

text=input("Enter the string:")
count=0
for w in text:
    count+=1
    # text.strip(w)
print(f"Length of {text}={count}")


# 4.Pattern print 
#         A 
#        B C 
#       D E F 
#      G H I J 
#     K L M N O

ascii_code=65 # A
for row in range(1,6):
    for space in range(row,5):
        print(" ",end="")
    for col in range(1,row+1):
        print(chr(ascii_code),end=" ")
        ascii_code+=1
    print()


# 3. Write a program to handling missing keys

dict={"name": "John", "age": 32, "place":"Ernakulam"}
search_key=input("enter the value :")
if search_key in dict:
    print(f"Value={ dict.get(search_key)}")
else:
    print("Value not found in the dictionary.")


