# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.



def list_orders(orders):
    for order in orders:
        print(order)
    for index, order in enumerate(orders):
        print(f'\nOrder {index + 1}: {order}')

orders = [
    ("Alex", "Laptop", 1),
    ("Vitoria", "Camera", 2),
    ("Jessica", "Car Phone Holder", 4),
    ("Nick", "Speaker", 1),
    ("Violet", "Backpack", 1),
    ("Matthew", "Gaming PC", 1),
]

list_orders(orders)
print("\nCurrent orders:", orders)

