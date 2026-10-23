orders = [
    {"order_id " : 101, "amount" : 1200, "status" : "Delivered"},
    {"order_id " : 102, "amount" : 2100, "status" : "cancelled"},
    {"order_id " : 103, "amount" : 800, "status" : "pending"},
    {"order_id " : 104, "amount" : 1800, "status" : "pending"},
    {"order_id " : 105, "amount" : 3200, "status" : "Delivered"},

]

total_sales = 0
delivered_count = 0
pending_count = 0

for order in orders:
    if order["status"] != "cancelled":
        total_sales += order["amount"]

    if order["status"] == "Delivered":
        delivered_count += 1

    elif order["status"] == "pending":
        pending_count +=1

print("Total orders:", len(orders))
print("Sales excluding cancelled orders:", total_sales)
print("Delivered orders:", delivered_count)
print("Pending orders:", pending_count)



