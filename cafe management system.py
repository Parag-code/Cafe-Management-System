# Menu dictionary
menu = {
    "Pizza": 100,
    "Pasta": 80,
    "Burger": 60,
    "Cold Coffee": 50,
    "Salad": 50,
    "Shake": 60,
    "Momos": 50
}

# Welcome message and menu display
print("Welcome to the Veg Spot Restaurant, Here is the menu: ")
print("Pizza: Rs100\nPasta: Rs80\nBurger: Rs60\nCold Coffee: Rs50\nSalad: Rs50\nShake: Rs60\nMomos: Rs50")

# Initialize order total
order_total = 0

# First order
item1 = input("Enter the name of item you want to order: ")

if item1 in menu:
    order_total += menu[item1]
    print(f"Your {item1} has been added to your order.")
else:
    print(f"{item1} is not available yet.")

# Ask if the customer wants to order another item
another_order = input("Do you want to order another item? (Yes/No): ")

# Check if user wants to order another item
if another_order == "Yes":
    item2 = input("Enter the name of item you want to order: ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your {item2} has been added to your order.")
    else:
        print(f"{item2} is not available yet.")
elif another_order == "No":
    print("No more items will be added to your order.")
else:
    print("Invalid input. Please enter 'Yes' or 'No'.")

# Display the order total
print(f"Your Order Total is Rs{order_total}.")

# Take payment method input
paymentmethod = input("What is your payment method? (Cash/Online): ")
print(f"You have to pay Rs{order_total} using {paymentmethod}.")

# Final message
print("Thanks For Coming!")