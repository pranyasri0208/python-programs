actual_cost=float(input("enter the actual cost:"))
sale_price=float(input("entter the sale price:"))
if (sale_price>actual_cost):
    profit=sale_price-actual_cost
    print("profit is", profit)
else:
    print("no profit")
