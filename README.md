# Cafe-Management-System
## Project Overview

This **Cafe Management System** is a simple Python-based program designed to simulate the ordering process at a restaurant or cafe. Customers can view the menu, order items, and choose a payment method. The system keeps track of the total order amount and displays the final cost, including the payment method.

The application is designed to be user-friendly and allows customers to:
- Order items from the menu.
- Add multiple items to their order.
- Choose a payment method (Cash or Online).
- View the final order total.

## Features
- Display of available menu items along with their prices.
- Ability to add multiple items to the order.
- Validation of available menu items.
- User-friendly interaction (order more, cancel order).
- Final order total and payment method selection.
- Supports basic input validation (for payment method).

## Technologies Used
- **Python**: The program is written in Python.
- **Basic Terminal/Console Input**: The program runs via terminal or command-line interface (CLI).

## How to Run the Program

### Prerequisites
- Ensure that you have **Python** installed on your system. You can download it from [here](https://www.python.org/downloads/).
- The program works on any operating system (Windows, macOS, Linux) that supports Python.

### Steps to Run:
1. **Clone or Download the Repository**:
    - Clone the repository using the following command:
    ```bash
    git clone <repository_url>
    ```
    Or simply download the files from the repository.

2. **Navigate to the Project Directory**:
    - Use your terminal or command prompt to navigate to the directory where the `cafe_management.py` file is saved.

3. **Run the Python Program**:
    - Execute the script using Python:
    ```bash
    python cafe_management.py
    ```

4. **Follow the On-Screen Instructions**:
    - The program will display a welcome message, followed by the menu, and prompt you to start ordering.
    - Follow the on-screen prompts to order items and choose a payment method.

Code Explanation

Menu:
The menu is represented as a dictionary in Python where the key is the item name (e.g., "Pizza") and the value is the price of the item in Indian Rupees (Rs).

Order Process:
The user enters the name of an item they want to order.
If the item exists in the menu, it is added to the order total.
The user can continue to add items or finish the order.
The system calculates the total order amount and displays it.
The user is asked for their payment method (Cash or Online), and the system confirms the total and payment method.
Input Validation:
The program checks if the ordered item is available on the menu.
Ensures the payment method is either "Cash" or "Online".
The order total is calculated and displayed based on the user's choices.
Enhancements and Future Work
This project is a basic implementation and can be enhanced with the following features:

GUI Interface: Implementing a graphical user interface (GUI) using libraries like Tkinter or PyQt to make the program more user-friendly.
Order History: Implementing a feature to store past orders and show the user’s order history.
Inventory Management: Adding functionality to track item availability and update the menu dynamically based on stock.
Advanced Input Validation: Further improving input validation to handle edge cases such as invalid item names or prices.
Payment Processing: Integrating payment gateway APIs for real online transactions.

License
This project is open-source and available under the MIT License.

Acknowledgments
Python documentation and tutorials were used to understand and implement the basic functionality.
No external libraries or dependencies were used in this basic version of the project.




