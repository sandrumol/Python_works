
lst=[5,2,4,1]
for i in range(len(lst)):
    for j in range(len(lst)-1):
        if lst[i]<lst[j]:
            temp=lst[i]
            lst[i]=lst[j] 
            lst[j]=temp
print(lst)