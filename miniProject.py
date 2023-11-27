clients = {
    1: {
        "pin": 9187,
        "name": "Aaliyah",
        "balance": 250000,
    },
    2: {
        "pin": 6342,
        "name": "Xavier",
        "balance": 12500,
    },
    3: {
        "pin": 7459,
        "name": "Imani",
        "balance": 30000,
    },
    4: {
        "pin": 5310,
        "name": "Angel",
        "balance": 800000,
    },
    5: {
        "pin": 2894,
        "name": "Cassandra",
        "balance": 40000,
    },
    6: {
        "pin": 4071,
        "name": "Chantelle",
        "balance": 15000,
    },
    7: {
        "pin": 8625,
        "name": "Elijah",
        "balance": 220000,
    },
    8: {
        "pin": 1748,
        "name": "Malik",
        "balance": 10000,
    },
    9: {
        "pin": 9364,
        "name": "Gabrielle",
        "balance": 28000,
    },
    10: {
        "pin": 5729,
        "name": "Christopher",
        "balance": 90500,
    }
}
def display_balance(client_name):
    
    for client_id, client_info in clients.items():
        if client_info["name"].lower() == client_name.lower():
            amount = format(client_info['balance'], ".2f")
            print(f"{client_name}, your current balance is: ${amount}")

def deposit_money(client_name):
    for client_id, client_info in clients.items():
        if client_info["name"].lower() == client_name.lower():
            amount = client_info['balance']
    deposit = float(input("Enter amount you would like to deposit: "))  # Use float instead of int
    amount += deposit
    amount = round(amount, 2)
    for client_id, client_info in clients.items():
        if client_info["name"].lower() == client_name.lower():
            client_info['balance'] = amount

    print(f"{client_name}, your new balance is: ${amount:.2f}")

def withdraw_money(client_name):
    for client_id, client_info in clients.items():
        if client_info["name"].lower() == client_name.lower():
            amount = client_info['balance']
    
    print("You have chosen to withdraw money:")
    print("Options for withdrawal: ")
    print("(1) 20")
    print("(2) 40")
    print("(3) 60")
    print("(4) 80")
    print("(5) 100")
    print("(6) Custom")
    option = int(input("Please select from the options by inputting a number from 1-6: "))
    
    withdrawal_amount = 0

    if option == 1:
        withdrawal_amount = 20
    elif option == 2:
        withdrawal_amount = 40
    elif option == 3:
        withdrawal_amount = 60
    elif option == 4:
        withdrawal_amount = 80
    elif option == 5:
        withdrawal_amount = 100
    elif option == 6:
        custom_amount = float(input("Enter how much you would like to withdraw: "))  # Use float instead of int
        if custom_amount > amount:
            print("Insufficient Funds! You don't have enough money!")
            return  # Return to avoid further processing
        else:
            withdrawal_amount = custom_amount
    else:
        print("Input not valid")
        return

    amount -= withdrawal_amount
    amount = round(amount, 2)

    for client_id, client_info in clients.items():
        if client_info["name"].lower() == client_name.lower():
            client_info['balance'] = amount

    print(f"{client_name}, your new balance is: ${amount:.2f}")


def main_menu(client_name):
    while True:
        print("Options menu: ")
        print("Enter 1 to display your current balance")
        print("Enter 2 to make a withdrawal")
        print("Enter 3 to make a deposit")
        print("Enter 4 to end this transaction")
        choice = int(input("Enter what you would like to do: "))
        if choice == 1:
            display_balance(client_name)
        elif choice == 2:
            withdraw_money(client_name)
        elif choice == 3:
            deposit_money(client_name)
        elif choice == 4:
            print("You are exiting the transaction! Have a good day!")
            break
        else:
            print("That is not an option please select again!")
# Print hello Humber bank terminal
def bank_info():
    counter = 0
    print("Hello welcome to Humber Bank Terminal!")
    name = input("Please enter your name: ")

    for client_id, client_info in clients.items():
        if client_info["name"].lower() == name.lower():
            print(f"Welcome back, {client_info['name']}!")
            while counter < 3:
                pin = int(input("Please enter 4-digit pin to access your bank account: "))
                if client_info["pin"] == pin:
                    print("Access granted!")
                    main_menu(client_info['name'])
                    break
                elif client_info["pin"] != pin:
                    counter += 1
                    attempts = 3 - counter
                    if attempts > 0:
                        print(f"Incorrect password. Please try again! You have {attempts} attempts left!")
                    else:
                        print(f"ACCESS DENIED!! ALARM WILL SOUND!! ACCOUNT HOLDER WILL BE NOTIFIED!!")
            break
    else:
        print("Client name not found!")


# Call the bank_info function
bank_info()

