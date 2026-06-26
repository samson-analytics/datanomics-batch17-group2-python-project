# 2)	Write a program that:
# •	Has a predefined dictionary of groceries with prices.
# •	Lets the user "add" items by typing their names.
# •	For each valid item, asks for the quantity.
# •	Keeps adding to the cart until the user types "checkout".
# •	Displays a final bill: each item, quantity, subtotal, and total.

def grocery_shopping():
    groceries ={"apple": 0.5, "banana": 0.3, "milk": 1.2, "bread": 1.5, "eggs": 2.0};

    print("Welcome to the Grocery Store!")
    print("Please add items to your cart by typing their names (type 'checkout' to finish):")
    for item in groceries:
        print(f"{item} - ${groceries[item]:.2f}")

    choice = input("Enter item name: ").lower()
    cart = {}

    while choice != "checkout":
        if choice in groceries:
            quantity = int(input(f"How many {choice}s would you like to add? "))
            if quantity > 0:
                cart[choice] = cart.get(choice, 0) + quantity
                print(f"Added {quantity} {choice}(s) to your cart.")
            else:
                print("Quantity must be greater than 0.")

        else:
            print("Item not found. Please try again.")
        choice = input("Enter item name (or 'checkout' to finish): ").lower()
    if choice == "checkout":
        print("\nFinal Bill:")
        total = 0
        for item, quantity in cart.items():
            subtotal = groceries[item] * quantity
            total += subtotal
            print(f"{item} x {quantity} - ${subtotal:.2f}")
        print(f"\nTotal: ${total:.2f}")
grocery_shopping()
