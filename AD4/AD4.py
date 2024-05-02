import json

def write_order():
    order = {}

    order["id"] = input("Enter order id: ")
    order["product_no"] = input("Enter product number: ")
    order["product_name"] = input("Enter product name: ")
    order["price"] = input("Enter price: ")

    filename = 'order_{}.json'.format(order["id"])

    f = open(filename, 'w')
    json.dump(order, f, indent=4) 

    f.close()

    print(f"Order {order['id']} saved successfully!")

def read_order():
    order_id = input("Enter order id to search: ")

    filename = 'order_{}.json'.format(order_id) 

    try:
        f = open(filename, 'r')
        order = json.load(f)

        print(f"Order {order_id} details:")
        for key, value in order.items():
            print(f"{key}: {value}")

        f.close()

    except FileNotFoundError:
        print(f"Order {order_id} not found!") 

def main():
    while True:
        print("\n1. Write Order")
        print("2. Read Order")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            write_order()
        elif choice == '2':
            read_order()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

main()
