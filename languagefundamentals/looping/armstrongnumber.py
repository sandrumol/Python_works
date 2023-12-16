# print armstrong number or not 
#  amstrong number => num=153
#                    sum=1**3+5**3+3**3=153
#                    num=1634
#                    sum=1**4+6**4+3**4+4**4=1634

num=input("Enter the number:")
digit_count=len(num) # len()=>provide length of string, it cannot be used in int
num=int(num)
original_num=num
sum=0

while(num!=0):
    digit=num%10
    sum=sum+digit**digit_count
    num=num//10

print(f"{original_num} is an armstrong number" if original_num==sum else f"{sum} is not an armstrong number")
