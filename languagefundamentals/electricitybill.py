#calculate electricity bill

# Energy Charge (Ec)= Unit Consumed X Unit Rate
# Fixed Charge (Fc)= Sanction Load X Fixed Charge Rate
# Electricity Duty (Ed)= (Energy Charge + Fixed Charge)X Tax Rate/100
# Total Electricity Bill= Energy Charge+ Fixed Charge+ Electricity Duty
# unit rate for 0 - 50 Unit=Rs. 2.0, 51 - 100 Unit=Rs. 2.50
# 0 - 150 Unit=Rs. 2.75, 151 - 250 Unit=Rs. 5.25
# 251 - 500 Unit=Rs. 6.30, 501 - 800 Unit=Rs. 7.10
# Above 801 Unit=Rs. 7.10, Commercial=Rs. 7.52

unit_consumed=int(input("Enter the unit consumed:"))
unit_rate=float(input("Enter the unit rate:"))
no_of_days=int(input("Enter the number of days:"))
energy_charge=unit_consumed*unit_rate

# tax rate on electricity bill in kerala is 10%
electricity_bill=(energy_charge)*(10/100)

total_electricity_bill=electricity_bill*no_of_days
print(f"Total electricity bill={total_electricity_bill}")