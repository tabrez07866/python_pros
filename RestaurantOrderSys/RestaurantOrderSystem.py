menu={
    1:("Pizza",120),
    2:("Burger",60),
    3:("Tea",12)
}

order=[]

def display_menu():
    print("\n 😋 Menu")
    for id,item in menu.items():
        print(f"{id}. {item[0]} - ${item[1]}")

def take_order():
    while True:
        display_menu()
        choice=int(input("Enter item number to order (0 to finish): "))

        if choice==0:
            break
        if choice in menu:
            order.append(menu[choice])
            print(f"✅ Added {menu[choice][0]}")
        else:
            print("❌ Invalid choice.")

def show_bill():
    total=0
    print("\n Your Order: ")
    for item in order:
        print(f"{item[0]} - ${item[1]}")
        total+=item[1]

    print(f"Total: ${total}")

take_order()
show_bill()