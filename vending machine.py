import random
from prettytable import PrettyTable

# List of all the  items which are  available and are  categorized  by their own type
items_available = [
    {"code": 1, "name": "doritos nachos cheese", "Price": 50, "stocks": 15, "category": "snack"},
    {"code": 2, "name": "cheetos crunchy", "Price": 40, "stocks": 10, "category": "snack"},
    {"code": 3, "name": "oreos", "Price": 30, "stocks": 13, "category": "snack"},
    {"code": 4, "name": "snickers", "Price": 35, "stocks": 11, "category": "snack"},
    {"code": 5, "name": "kitkat", "Price": 25, "stocks": 15, "category": "snack"},
    {"code": 6, "name": "Reeses Peanut Butter Cups", "Price": 55, "stocks": 9, "category": "snack"},
    {"code": 7, "name": "pringles", "Price": 89, "stocks": 13, "category": "snack"},
    {"code": 11, "name": "pepsi", "Price": 50, "stocks": 12, "category": "soft drink"},
    {"code": 22, "name": "coca cola", "Price": 45, "stocks": 10, "category": "soft drink"},
    {"code": 33, "name": "sprite", "Price": 55, "stocks": 11, "category": "soft drink"},
    {"code": 44, "name": "fanta", "Price": 50, "stocks": 12, "category": "soft drink"},
    {"code": 55, "name": "nescafe cold coffee", "Price": 40, "stocks": 15, "category": "soft drink"},
    {"code": 66, "name": "red bull", "Price": 45, "stocks": 10, "category": "soft drink"},
    {"code": 77, "name": "aquafina", "Price": 30, "stocks": 11, "category": "soft drink"},
]


# Displaying all the  items in a table format with the help of pretty tables.
def display_items(items):
    
    table = PrettyTable()
    table.field_names = ["Code", "Name", "Price", "stocks", "category"]                                  # headers of the table.
    for item in items:
        table.add_row([item["code"], item["name"], item["Price"], item["stocks"], item["category"]])     # rows,containing all the information details of the item.
    print(table)


# Suggest complementary items.
def suggest_item(selected_item):
    """Suggest a complementary item based on the selected item's category."""
    complementary_items = []
    if selected_item["category"] == "snack":
        complementary_items = [item for item in items_available if item["category"] == "soft drink" and item["stocks"] > 0]
    elif selected_item["category"] == "soft drink":
        complementary_items = [item for item in items_available if item["category"] == "snack" and item["stocks"] > 0]

    if complementary_items:
        suggestion = random.choice(complementary_items)
        print(f"Would you like to try {suggestion['name']} for just {suggestion['Price']}? It's a great combo!")


# Main working of vending machine.
def vending_machine(items):                                                       # main function which handles the function of vending machine .
    
    selected_items = []

    print("Items available:")                                                     # it displays the list of all the item available.
    display_items(items)                                                          # calling display item function.
    print("\n**** Choose your desirable item ****\n")

    #loop,so user can add unlimited items in their cart.
    while True:
        try:
            # asking the user to input the code of the item they want to buy.
        
            buy_item_code = int(input("\nEnter the code of the item you would like to buy: "))
            item_found = next((item for item in items if item["code"] == buy_item_code), None)

            if item_found:
                if item_found["stocks"] > 0:                                        # if the item is found in the stock then it gets added to the cart
                    item_found["stocks"] -= 1                                       # automatically the stocks decreases.
                    selected_items.append(item_found)
                    print(f"{item_found['name']} is added to your cart.")           #print a message regarding addition of the item to the cart.
                    suggest_item(item_found)  # Suggest complementary item.
                else:
                    print("Oops, this item is out of stock right now.")             # else it will print this informing the user
            else:
                print("Invalid input. Please enter a valid item code.")             # it will print this option when input is invalid.
        except ValueError:
            print("Invalid input. Please enter a valid number.")                    # if the value is not an interger.

        # Ask if the individual wants to add more items.
        more_items = input("\nType any key to add more items to your cart, or type 'finish' if you are done: ").lower()
        if more_items == "finish":
            break

    # Before finalizing the transaction, suggest a complementary item for each item in the cart.
    if selected_items:
        print("\nBased on your selections, we have some complementary item suggestions:")
        for selected_item in selected_items:
            suggest_item(selected_item)

    
    # Calculate the total cost. 
    total_cost = sum_items(selected_items)                                          # it calculates the total cost the selected items                                 
    print(f"\nThe total cost of your selected items is: {total_cost}")              #it will display the total cost.

    
    
    # Handle payment.
    if handle_payment(total_cost):                                        
        
        print("\n your Payment is successful!")                                             #it will display this message if the payment was successful.

        # Ask the user if they want the full bill or just the total sum.
        while True:
            receipt_choice = input("\n11. Print the full bill\n22. Print only the total sum\nChoose 11 or 22: ")      #promp the user to choose one of these options.
            if receipt_choice == "11":
                print(create_receipt(selected_items))                              #if user choose2 11 it will print the whole receipt.
                break
            elif receipt_choice == "22":
                print(f"Total: {total_cost}")                                      #if the user chooses 22 it will print the total cost.
                break                                                              # and it will break the loop.
            else:
                print("Invalid input. Please enter either 11 or 22.")              #  else if the input is invalid then it will ask user to input again. 

        # Display all the remaining stocks.
        print("\nRemaining stocks:")
        display_items(items)

    print("\nThank you for using our Hunger Machine!")



# Generating the receipt.
def create_receipt(items):                                                       # function which helps to generate a reciept.

    receipt = "\t\tPRODUCT -- COST\n"                               
    total = 0                                                                     # begining the total at 0
    for item in items:
        receipt += f"\t{item['name']} -- {item['Price']}\n"                       # it adds the the item name and its price  
        total += item["Price"]                                                    # it adds the price of the item to the total.
    receipt += f"\n\tTotal: {total}\n"                                            # Adds the total cost at the end of the receipt. 
    return receipt




# Handling the payment procedure

def handle_payment(total_amount):
    
    while True:                                                        # it will keep on looping until user input correct input.
        try:
            amount_paid = float(input(f"\nThe total amount is {total_amount}. Enter the amount you are paying: "))    #user is asked to enter the amount of money user is paying.
            if amount_paid >= total_amount:                            #if the amount pais is more than the total amount.
                change = amount_paid - total_amount
                if change > 0:                   
                    print(f"\nThank you! Your total amount of change is {change:.2f}.")
                else:
                    print("\nThanks for the payment!")                 #it will print this if amount paid by the user is equal to total amount.
                return True
            else:                                                      #if the payment is not sufficient.
                deficit = total_amount - amount_paid
                print(f"\nNot enough payment. Please pay {deficit:.2f} more.")
        except ValueError:
            print("\nInvalid input. Please enter a valid amount.")


# This sum_items function calculates the total cost of all the items that user has added to their cart.
def sum_items(items):
  return sum(item["Price"] for item in items)


# calling the vending machine function.
vending_machine(items_available)






