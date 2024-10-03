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

        #if option == 4: # Transfer Money

        #if option 



########
        if option == 4:
        def transfer_money():
            print("Accounts available:")
    for people in people.keys():
        print(people)
    
    sender = input("Enter the name of the sender: ")
    recipient = input("Enter the name of the recipient: ")
    
    if sender not in people:
        print(f"Sender '{sender}' not found.")
        return main()
    
    if recipient not in people:
        print(f"Recipient '{recipient}' not found.")
        return main()
    
    amount = float(input("Enter the amount to transfer: $"))
    
    if amount > people[sender]:
        print(f"Insufficient balance in {sender}'s account.")
    else:
        people[sender] -= amount
        people[recipient] += amount
        print(f"Transferred ${amount} from {sender} to {recipient}.")
        print(f"New balance for {sender}: ${people[sender]}")
        print(f"New balance for {recipient}: ${people[recipient]}")

    main()

def leave_program():
    check = True
    while check:
        print("Would you like to leave the program?")
        desc = input("Yes or No?: ").lower()

        if desc == "yes":
            exit()
        elif desc == "no":
            main()
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

main()
        
    




#######

    #if option == 6:
        



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
