# Name: --------- (cause it's on GitHub ( ͡° ͜ʖ ͡°))
# Section: 275-02
# Desc: Lab4

people = {
    "Fin": 5,
    "Dylan": 10,
    "Mrbasmachi": 15
}

# Main function to drive the program
def main():
    check = True
    while check:
        print("Who are you?: ")
        name_enter = input("Enter your name: ")  # Prompt user for name

        if name_enter not in people:
            print("Account not found. Please create an account.")
            continue  # Skip to next iteration if account not found

        # Display options
        print("What do you want to do?: ")
        print("1. Deposit")          
        print("2. Withdraw")
        print("3. List all accounts")
        print("4. Transfer Money")
        print("5. Add/Remove an account")
        print("6. Leave the Program")
        
        option = int(input("Enter your option: "))  # Prompt user for input of operation

        # Call the appropriate function based on the option
        if option == 1:
            deposit(name_enter)
        elif option == 2:
            withdraw(name_enter)
        elif option == 3:
            list_accounts()
        elif option == 4:
            transfer(name_enter)
        elif option == 5:
            add_remove()
        elif option == 6:
            leave_program()



# Function to handle deposit
def deposit(name_enter):
    amount = int(input("How much to Deposit: "))  # Prompt for deposit amount
    people[name_enter] += amount  # Add the deposit to the user's balance
    print(f"New balance for {name_enter}: {people[name_enter]}")




# Function to handle withdrawals
def withdraw(name_enter):
    amount = int(input("How much to Withdraw: "))  # Prompt for withdrawal amount
    if amount <= people[name_enter]:
        people[name_enter] -= amount  # Deduct the amount from the balance
        print(f"New balance for {name_enter}: {people[name_enter]}")




# Function to list all accounts and their balances
def list_accounts():
    print("Current accounts and balances:")
    for account, balance in people.items():
        print(f"{account}: {balance}")




# Function to transfer money between accounts
def transfer(name_enter):
    recipient = input("Enter the name of the account to transfer to: ")  # Prompt for recipient
    if recipient not in people:
        print("Recipient account not found.")
        return
    
    amount = int(input("Enter the amount to transfer: "))  # Prompt for transfer amount
    if amount <= people[name_enter]:
        people[name_enter] -= amount  # Deduct from sender
        people[recipient] += amount  # Add to recipient
        print(f"Transferred {amount} from {name_enter} to {recipient}.")
        print(f"New balance for {name_enter}: {people[name_enter]}")
        print(f"New balance for {recipient}: {people[recipient]}")
    else:
        print("Insufficient funds.")





# Function to add or remove accounts
def add_remove():
    action = input("Would you like to Add or Remove an account? (A/R): ").lower()  # Prompt for action
    
    if action == 'a':
        new_account = input("Enter the new account name: ")
        initial_balance = int(input("Enter the initial balance: "))  # Prompt for initial balance
        people[new_account] = initial_balance  # Add the new account
        print(f"Account {new_account} added with balance {initial_balance}.")
    
    elif action == 'r':  # Removing an account
        account_to_remove = input("Enter the account name to remove: ")
        if account_to_remove in people:
            del people[account_to_remove]  # Remove the account
            print(f"Account {account_to_remove} removed.")
        else:
            print("Account not found.")
    else:
        print("Invalid option. Please enter 'A' or 'R'.")





# Function to handle exiting the program
def leave_program():
    desc = input("Would you like to leave the program? (Yes/No): ").lower()
    if desc == "yes":
        print("Exiting the program...")
        exit()  # Exit the program
    elif desc == "no":
        print("Returning to main...")
        main()  # Return to main function
    else:
        print("Invalid input, please answer 'Yes' or 'No'.")
        leave_program()  # Re-run the function if input is invalid









# Start the program
if __name__ == "__main__":
    main()


"""
    deposit(name_enter)
    withdraw(name_enter)
    list_accounts()
    transfer(name_enter)
    add_remove()
    leave_program()


The main loop calls the appropriate function based on the option selected by the user

functions directly interact with the global people hashmap

"""