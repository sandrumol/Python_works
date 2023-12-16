# 1.Write a python program to convert the temperature in degree centigrade to fahrenheit

#  F = (C × 9/5) + 32
celsius=int(input("Enter the value:"))
fahrenheit=(celsius*(9/5))+32
print(fahrenheit)


# 2. Write a python program to find compound interest

# A=P*((1+(r/100))**t)  # A=Total Accumulated Amount
# C.I=A-P
P=int(input("Enter the Principal Amount:")) # 50,000
r=int(input("Enter the Rate of Interest:")) # 10%
t=int(input("Enter the Time in years:"))  # 5 years 
A=P*((1+(r/100))**t)
compound_interest=A-P
print(f"Compound interest=Rs. {compound_interest}") #30525.50


# 3. Write a python program to find area of a circle.

# area=pi*r**2
radius=int(input("Enter the radius:"))
pi=3.14
area=pi*radius**2
print(f"Area of circle with radius {radius} is {area}")
