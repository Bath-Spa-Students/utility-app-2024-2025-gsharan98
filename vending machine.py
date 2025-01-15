print("\n**** Welcome to HUNGER MACHINE ****\n")  # Welcome message
from prettytable import PrettyTable

# List of snacks available in the vending machine.
snacks_available = [
    {"code": 1, "name": "doritos nachos cheese", 'Price': 50, "stocks": 15},
    {"code": 2, "name": "cheetos crunchy", 'Price': 40, "stocks": 10},
    {"code": 3, "name": "oreos", 'Price': 30, "stocks": 13},
    {"code": 4, "name": "snickers", 'Price': 35, "stocks": 11},
    {"code": 5, "name": "kitkat", 'Price': 25, "stocks": 15},
    {"code": 6, "name": "Reeses Peanut Butter Cups", 'Price': 55, "stocks": 9},
    {"code": 7, "name": "pringles", 'Price': 89, "stocks": 13},
    {"code": 11, "name": "pepsi", 'Price': 50, "stocks": 12},
    {"code": 22, "name": "coca cola", 'Price': 45, "stocks": 10},
    {"code": 33, "name": "sprite", 'Price': 55, "stocks": 11},
    {"code": 44, "name": "fanta", 'Price': 50, "stocks": 12},
    {"code": 55, "name": "nescafe cold coffee", 'Price': 40, "stocks": 15},
    {"code": 66, "name": "red bull", 'Price': 45, "stocks": 10},
    {"code": 77, "name": "aquafina", 'Price': 30, "stocks": 11},
]

# Displaying all the items in a table format using PrettyTable.
table = PrettyTable()
table.field_names = ["Code", "Name", "Price", "Stocks"]
for item in snacks_available:
    table.add_row([item["code"], item["name"], item["Price"], item["stocks"]])

print("Snacks available:")
print(table)

# Main working of vending machine.
def vending_machine(snacks):
    """Main function for the vending machine."""
    selected_items = []

    print("**** Choose your desirable item ****\n")
    
    while True:
        try:
            # Asking user to input the code of the item they want to buy.
            buy_item_code = int(input("\nEnter the code of the snack you would like to buy: "))
            item_found = next((item for item in snacks if item["code"] == buy_item_code), None)

            if item_found:
                if item_found["stocks"] > 0:
                    item_found["stocks"] -= 1
                    selected_items.append(item_found)
                    print(f"{item_found['name']} is added to your cart.")
                else:
                    print("Oops, this item is out of stock right now.")
            else:
                print("Invalid input. Please enter a valid snack code.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Asking if the individual wants to add more items.
        more_items = input("\nType any key to add more items to your cart, or type 'finish' if you are done: ").lower()
        if more_items == "finish":
            break

    # Calculating the total cost.
    total_cost = sum_items(selected_items)
    print(f"\nThe total cost of your selected items is: {total_cost}")

    # Payment process.
    if handle_payment(total_cost):
        print("\nPayment successful!")

        # Asking the user if they want the full bill or just the total sum.
        while True:
            receipt_choice = input("\n11. Print the full bill\n22. Print only the total sum\nChoose 11 or 22: ")
            if receipt_choice == "11":
                print(create_receipt(selected_items))
                break
            elif receipt_choice == "22":
                print(f"Total: {total_cost}")
                break
            else:
                print("Invalid input. Please enter either 11 or 22.")

        # Displaying the remaining stocks.
        print("\nRemaining stocks:")
        for item in snacks:
            print(f"{item['name']} -- {item['stocks']} left.")

    print("\nThank you for using our Hunger Machine!")

# Generating the receipt.
def create_receipt(items):
    """Generate the receipt of purchased items."""
    receipt = "\t\tPRODUCT -- COST\n"
    total = 0
    for item in items:
        receipt += f"\t{item['name']} -- {item['Price']}\n"
        total += item["Price"]
    receipt += f"\n\tTotal: {total}\n"
    return receipt

# Handling payment.
def handle_payment(total_amount):
    """Handles the payment process."""
    while True:
        try:
            amount_paid = float(input(f"\nThe total amount is {total_amount}. Enter the amount paid: "))
            if amount_paid >= total_amount:
                change = amount_paid - total_amount
                if change > 0:
                    print(f"\nThank you! Your total amount of change is {change:.2f}.")
                else:
                    print("\nThanks for the payment!")
                return True
            else:
                deficit = total_amount - amount_paid
                print(f"\nNot enough payment. Please pay {deficit:.2f} more.")
        except ValueError:
            print("\nInvalid input. Please enter a valid amount.")

# Calculating the total sum of selected items.
def sum_items(items):
    """Calculate the total sum of selected items."""
    return sum(item["Price"] for item in items)

# Running the vending machine.
vending_machine(snacks_available)