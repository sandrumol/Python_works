# arr=[1,4,3,5,6,7] find missing +ve number ans=2

arr=[1,3,5,4,6,7]
arr.sort()
i=0
while(i<len(arr)-1):               
    j=i+1
    difference=arr[j]-arr[i]
    if difference>1:
        print(f"missing element={arr[i]+1}")
        break
    i+=1



