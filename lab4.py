"""
Name: --------- (cause its on github ( ͡° ͜ʖ ͡°))
Section: 275-02
Desc: Lab4
"""
people = {
    "Fin": 5,
    "Dylan": 10,
    "Mrbasmachi": 15
}

def main():
    check = True
    while(check == True):
        print("Who are you?: ")
        name_enter = (input("enter your name: ")) # prompt - user for name

        
        print("What do you want to do?: ")
        print("1. Deposit")          
        print("2. Withdraw")
        print("3. List all accounts: ")
        print("4. Transfer Money: ")
        print("5. Add/Remove an account: ")
        print("6. Leave the Program: ")
        option = int(input("enter your option: ")) # prompt - user for input of operation
        
        if option == 1: # Deposit 
            account_name = input("How much to Deposit: ") # var for putting in money
            people[name_enter] += int(account_name)
            return print(people[name_enter])

        if option == 2: # Withdraw 
            account_name = input("How much to Withdraw: ") # var for taking out
            people[name_enter] -= int(account_name)
            return print(people[name_enter])
        
        if option == 3: # List the accounts
            print(people)

        elif option == 4:   # Transfer money to new accounts
            recipient = input("Enter the name of the account to transfer to: ") # Account to transfer the money
            if recipient not in people:
                print("Recipient account not found.")
                continue


            amount = int(input("Enter the amount to transfer: ")) # rlly confusting :3
            amount = int(input("Enter amount to transfer: "))   # like everything below

            if amount <= people[name_enter]:
                people[name_enter] -= amount
                people[recipient] += amount
                print(f"Transfered {amount} from {name_enter} to {recipient}")  # Printing What happens
                print(f"New balance for {name_enter}: {people[name_enter]}")
                print(f"New balance for {recipient}: {people[recipient]}")

            else:
                print("No funds...")


        elif option == 5:  # Add/Remove an account
            add_or_remove_action = input("Would you like to Add or Remove an account? (A/R): ").lower() # add_or_remove_action var for adding new accounts or removing them

            if add_or_remove_action == 'a':
                new_account = input("Enter the new account name: ")
                initial_balance = int(input("Enter the initial balance: ")) # var for adding a new balance if pressed a for add
                people[new_account] = initial_balance   # then add to the people dict. above
                print(f"Account {new_account} added with balance {initial_balance}.")   # now print the new account and the blaance you put in

            elif add_or_remove_action == 'r':   # if the person wants to remove a account
                account_to_remove = input("Enter the account name to remove: ")

                if account_to_remove in people: 
                    del people[account_to_remove]   # del for deleting a person out of the people dict.
                    print(f"Account {account_to_remove} removed.")  # print ^^^

                else:
                    print("Account not found.")

            else:
                print("Invalid option. Please enter 'A' or 'R'.")
    


        if option == 6: # Start to leave the program
            leave_program()



def leave_program(): # exiting the program
    check = True
    while(check == True):
        print("Would you like to leave the program?")
        desc = str(input("Yes or No?: "))       # var for making a decision(didnt want to use option again)
        
        if desc.lower() == "yes":
            print("Exiting the program...")
            exit()  # var to exit the program
        
        if desc == "no":
            print("Returning to main...")
            main()

        else:
            print("Wront input...")
            leave_program() # Re-runs the "leave_program" function again    
        
    
        
        

if __name__ == "__main__":
    main()
    leave_program()







"""
def deposit()
def ...
def ..
def ...

make functions for everything
call them when selecting things

"""


#elif account_name in accounts:
            #amount = float(input("Enter amount you want to enter: "))
            #           amount = float(input("Enter amount to deposit: "))
        # elif option == 2: # Transfer
