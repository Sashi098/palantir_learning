orders = [1200, 2500, 800, 3200, 1800]

total_sales = sum(orders)
total_orders = len(orders)
average_orders = total_sales / total_orders
highest_order = max(orders)
lowest_order = min(orders)

print("Total_sales : ", total_sales)
print("Total_orders : ", total_orders)
print("Average_orders : ", average_orders)
print("Highest_order : ", highest_order)
print("Lowest_order : ", lowest_order)