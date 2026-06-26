#1)	Build a program that:
# •	Displays a list of snacks and drinks with item numbers and prices.
# •	Ask the user to choose items by number in a loop.
# •	 Keeps track of selected items and their prices.
# •	Ends when the user types "done".
# •	Finally prints a receipt showing: List of selected items with prices and total cost

menu = {
    1: {"name": "chocholate", "price": 2},
    2: {"name": "chips", "price": 1},
    3: {"name": "cookies", "price": 5},
    4: {"name": "water", "price": 4},
}

for number, item in menu.items():
    print(number, ".", item["name"], "-", "$", item["price"])

selected_items = []

while True:
    choice = input ("Enter item number or 'done': ")

    if choice == "done":
        break

    choice = int(choice)
    selected_items.append(menu[choice])

total_price = 0

for item in selected_items:
    print(item["name"], "-", "$", item["price"])

    total_price += item["price"]

print("\nTotal Price is: ", "$", total_price)
