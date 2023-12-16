# 1.Write a program to print 10,8,6,4,2,0,-2,-4,-6,-8,-10

# num=10
# while(num>=-10):
#     if num%2==0:
#         print(num,end=",")
#     num-=1


# 2. Write a program to print sum of even number in a range

start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
sum=0
for i in range(start,end):
    if i%2==0:
        sum=sum+i
print(f"Sum of even numbers={sum}")


# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’’

weight_in_kg=int(input("Enter the weight in kg:"))
height_in_cm=int(input("Enter the height in cm:"))
height_in_meter=(height_in_cm/100)
bmi=(weight_in_kg)/(height_in_meter**2)
if bmi<18.5:
    print("Underweigt")
elif bmi<25:
    print("Healthy")
elif bmi>=25:
    print("Overweight")

