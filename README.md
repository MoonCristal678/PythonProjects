# PythonProjects
### Overview:
EDUCATIONAL PURPOSE ONLY 

This Python script simulates a basic banking terminal for Humber Bank. It uses a dictionary named `clients` to store information about individual clients, including their account number, PIN, name, and balance. The script provides functionalities such as displaying account balance, depositing money, and withdrawing money. Users interact with the terminal by entering their name and PIN.

### `display_balance(client_name)`:

This function takes a client's name as input, searches for the corresponding client in the `clients` dictionary, and displays their current account balance in a formatted manner.

### `deposit_money(client_name)`:

This function allows a client to deposit money into their account. It prompts the user to enter the deposit amount, updates the account balance, and displays the new balance.

### `withdraw_money(client_name)`:

This function facilitates withdrawals from a client's account. It presents a menu of withdrawal options, including a custom amount. After the user selects an option, it deducts the corresponding amount from the account balance and displays the new balance. It includes checks for insufficient funds and invalid inputs.

### `main_menu(client_name)`:

This function serves as the main menu for the banking terminal. It continuously prompts the user with options to display balance, make a withdrawal, make a deposit, or end the transaction. The user's choice determines which corresponding function is called.

### `bank_info()`:

This function initiates the banking terminal. It greets the user, prompts for their name, and verifies their identity using a PIN. If the user fails to enter the correct PIN within three attempts, access is denied with a warning. Upon successful verification, the main menu is presented.

### Additional Notes:

- The script uses a simple dictionary-based approach to store client information.
- It includes basic input validation, such as checking for incorrect PINs and invalid menu choices.
- The withdrawal function offers predefined withdrawal amounts as well as a custom amount option.
- The script provides a welcome message and tracks unsuccessful login attempts.

### How to Use:

1. Run the script.
2. Enter your name when prompted.
3. Enter your 4-digit PIN.
4. Choose from the menu options (display balance, withdraw, deposit, or end the transaction).
5. Follow the prompts to complete the selected action.

Note: This is a simplified simulation and may not cover all aspects of a real-world banking system, such as security measures and transaction logging.