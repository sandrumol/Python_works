prev=0
current=1
print(f"{prev} {current}",end=" ")
for i in range(0,10):
    next=prev+current
    print(next,end=" ")
    prev=current
    current=next
    