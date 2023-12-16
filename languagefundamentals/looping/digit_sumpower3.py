num=1634
sum=0
while(num!=0):
    digit=num%10
    sum=sum+(digit**4)
    num=num//10
print(sum)

# amstrong number => num=153
#                    sum=1**3+5**3+3**3=153
#                    num=1634
#                    sum=1**4+6**4+3**4+4**4