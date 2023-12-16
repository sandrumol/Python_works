# arr=[2,5,3,6,1,4] sum=10   res=6,4  

lst=[3,4,5,2,6]
sum=int(input("Enter the sum:"))
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         curr_sum=lst[i]+lst[j]
#         if sum==curr_sum:
#             print(lst[i],lst[j])
#             break


#  OR


# for i in range(0,len(lst)):
#     diff=sum-lst[i]
#     if diff in lst and diff!=lst[i] and diff>lst[i]:
#         print(lst[i],diff)
        
  

# OR

lst.sort()
low=0
upp=len(lst)-1
while(low<upp):                             # minimum complexity, fast execution
    curr_sum=lst[low]+lst[upp]
    if curr_sum==sum:       
        print(lst[low],lst[upp])
        low+=1
        upp-=1
    elif curr_sum<sum:
        low+=1
    elif curr_sum>sum:
        upp-=1


