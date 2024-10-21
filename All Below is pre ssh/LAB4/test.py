people = {
    "Alice": 1000,
    "Bob": 500,
    "Charlie": 300
}  # Predefined accounts and their balances

name_enter = None  # Initialize name_enter as a global variable

def main():
    global name_enter  # Declare that we are using the global variable
    check = True
    while check:
        print("Who are you?: ")
        name_enter = input("Enter your name: ")  # Prompt user for name

        # Check if the account exists; if not, prompt to create an account
        if name_enter not in people:
            print("Account not found.")
            create_account()  # Call function to create an account
            continue  # Restart the loop to allow the user to choose an action

        print("What do you want to do?: ")
        print("1. Deposit")          
        print("2. Withdraw")
        print("3. List all accounts")
        print("4. Transfer Money")
        print("5. Add/Remove an account")
        print("6. Leave the Program")
        
        option = int(input("Enter your option: "))  # Prompt user for input of operation
        
        if option == 1:  # Deposit 
            deposit()
        elif option == 2:  # Withdraw
            withdraw()
        elif option == 3:  # List the accounts
            print(people)
        elif option == 4:  # Transfer money to new accounts
            transfer()
        elif option == 5:  # Add/Remove an account
            add_remove()
        elif option == 6:  # Leave the program
            leave_program()
        else:
            print("Invalid option. Please try again.")

def create_account():
    global name_enter  # Access the global variable
    initial_balance = int(input(f"Enter the initial balance for {name_enter}: "))
    people[name_enter] = initial_balance  # Add the new account to the people dictionary
    print(f"Account {name_enter} created with an initial balance of {initial_balance}.")

def deposit():
    global name_enter  # Access the global variable
    account_name = int(input("How much to deposit: "))  # Amount to deposit
    people[name_enter] += account_name
    print(f"New balance for {name_enter}: {people[name_enter]}")

def withdraw():
    global name_enter  # Access the global variable
    account_name = int(input("How much to withdraw: "))  # Amount to withdraw
    if people[name_enter] >= account_name:
        people[name_enter] -= account_name
        print(f"New balance for {name_enter}: {people[name_enter]}")
    else:
        print("Insufficient funds.")

def transfer():
    global name_enter  # Access the global variable
    recipient = input("Enter the name of the account to transfer to: ")  # Account to transfer money to
    if recipient not in people:
        print("Recipient account not found.")
        return

    amount = int(input("Enter the amount to transfer: "))
    if people[name_enter] >= amount:
        people[name_enter] -= amount
        people[recipient] += amount
        print(f"Transferred {amount} from {name_enter} to {recipient}.")
        print(f"New balance for {name_enter}: {people[name_enter]}")
        print(f"New balance for {recipient}: {people[recipient]}")
    else:
        print("Insufficient funds.")

def add_remove():
    add_or_remove_action = input("Would you like to Add or Remove an account? (A/R): ").lower()
    
    if add_or_remove_action == 'a':
        new_account = input("Enter the new account name: ")
        initial_balance = int(input("Enter the initial balance: "))  # Initial balance for new account
        people[new_account] = initial_balance  # Add to the people dictionary
        print(f"Account {new_account} added with balance {initial_balance}.")
    
    elif add_or_remove_action == 'r':  # Remove an account
        account_to_remove = input("Enter the account name to remove: ")
        if account_to_remove in people: 
            del people[account_to_remove]  # Delete account from the dictionary
            print(f"Account {account_to_remove} removed.")
        else:
            print("Account not found.")
    else:
        print("Invalid option. Please enter 'A' or 'R'.")

def leave_program():
    desc = input("Would you like to leave the program? (Yes/No): ").lower()
    if desc == "yes":
        print("Exiting the program...")
        exit()  # Exit the program
    elif desc == "no":
        print("Returning to main...")
        main()  # Return to main function
    else:
        print("Wrong input...")
        leave_program()  # Re-run the function if the input is invalid    

if __name__ == "__main__":
    main()
