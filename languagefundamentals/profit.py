selling_price=int(input("Enter selling price:"))
cost_price=int(input("Enter cost price:"))

profit=selling_price-cost_price
print(f"profit is {profit}")

profit_percent=(profit/cost_price)*100
print(f"percentage of profit={profit_percent}%")