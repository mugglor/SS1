purchase = int(input("enter the amount of purchase: "))
stateSales = purchase * 0.05
countySales = purchase * 0.025
print("The amount of the purchase:", purchase)
print("The amount of the state sales:", stateSales)
print("The amount of the county sales:", countySales)
print("The amount of the total sales tax:", stateSales + countySales)
print("The amount of the total of the sale:", purchase + stateSales + countySales)
