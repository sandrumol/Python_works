# find duplicate numbers

arr=[4,9,4,5,6,9,5]
# arr.sort()
# print(arr)
# for i in range(0,len(arr)-1):
#     for j in range(i+1,len(arr)):
#         difference=arr[j]-arr[i]
#         if difference==0:
#             print(arr[i])

# OR

arr.sort()
# print(arr)
i=0
while(i<len(arr)-1):                #less complexity ,fast execution
    j=i+1
    difference=arr[j]-arr[i]
    if difference==0:
        print(arr[i])
        i=j
    i+=1
    
# OR

# arr.sort()
# print(arr)
# current=arr[0]
# for i in range(0,len(arr)):
#     if current==arr[i]:
#         print(arr[i])
#         curr=arr[i]
#     else:
#         current=arr[i]


#  OR

# arr.sort()
# print(arr)
# curr=arr[0]
# i=1
# while(i<len(arr)):
#     if curr==arr[i]:
#         print(arr[i])
#         curr=arr[i]
#     else:
#         curr=arr[i]
#     i+=1