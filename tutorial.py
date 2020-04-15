from pizzapy import Customer, StoreLocator, Order


def searchMenu(menu):
    print("You are now searching the menu...")

    item = input("Type an item to look for: ").strip().lower()

    if len(item) > 1:
        item = item[0].upper() + item[1:]
        print(f"Results for: {item}")
        menu.search(Name=item)
        print()
    else:
        print("No Results")


def addToOrder(order):
    print("Please type the codes of the items you'd like to order...")
    print("Press ENTER to stop ordering.")
    while True:
        item = input("Code:").upper()
        try:
            order.add_item(item)
        except:
            if item == "":
                break
            print("Invalid Code...")


customer = Customer("James", "Maddox", "james.maddox07@gmail.com",
                    "5029748198", "9433 Chambers Way, Louisville, KY, 40229")

my_local_dominos = StoreLocator.find_closest_store_to_customer(customer)
print(my_local_dominos)
print("\nMENU\n")

menu = my_local_dominos.get_menu()
order = Order.begin_customer_order(customer, my_local_dominos, "us")

while True:
    searchMenu(menu)
    addToOrder(order)
    answer = input("Would you like to add more items (y/n)? ")
    if answer.lower() not in ["yes", "y"]:
        break
