#bmi=weight_in_kg/(height_in_meter**2)

weight_in_kg=int(input("Enter the weight in kg:"))
height_in_cm=int(input("Enter the height in cm:"))
height_in_meter=(height_in_cm/100)

bmi=(weight_in_kg)/(height_in_meter**2)
if bmi<19:
    print("Underweigt")
elif bmi<25:
    print("Healthy")
elif bmi<30:
    print("Overweight")
elif bmi<40:
    print("Obesity")
else:
    print("Severe obese")
print(f"bmi={bmi}")

#OR
# if bmi<19:
#     print("Underweigt")
# elif bmi>=19 and bmi<25:
#     print("Healthy")
# elif bmi>=25 and bmi<30:
#     print("Overweight")
# elif bmi>=30 and bmi<40:
#     print("Obesity")
# else:
#     print("Severe obese")