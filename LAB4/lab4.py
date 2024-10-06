"""
Name: --------- (cause its on github ( ͡° ͜ʖ ͡°))
Section: 275-02
Desc: Lab4
"""

# list of people in a dictionary
people = {
    "Fin": 5,
    "Dylan": 10,
    "Mrbasmachi": 15
}


# function for selecting what to do in the program
def main():
    check = True
    while(check == True):
        print("Who are you?: ")
        name_enter = (input("enter your name: ")) # varible for stroing the users input name

        
        print("What do you want to do?: ")
        print("1. Deposit")          
        print("2. Withdraw")
        print("3. List all accounts: ")
        print("4. Transfer Money: ")
        print("5. Add/Remove an account: ")
        print("6. Print all the data to a .txt")
        print("7. Leave the Program: ")
        option = int(input("enter your option: ")) # prompt user for input of operation


        
        if option == 1: # Deposit 
             deposit(name_enter)
        if option == 2: # Withdraw 
             withdraw(name_enter)
        if option == 3: # List the accounts
            list_accounts()
        if option == 4:   # Transfer money to new accounts
             transfer(name_enter)
        if option == 5:  # Add/Remove an account
             add_remove()
        if option == 6:
              read_write_txt()
        if option == 7: # Start function to leave the program
             leave_program()





# Depositing money into one of the accounts in the 'people' dictionary
def deposit(name_enter):    # start of the deposit function 'name_enter' goes back to the name you chose
            input_money = input("How much to Deposit: ") # input_name looks for your input of money
            people[name_enter] += int(input_money) # Adds the number of money you put in in input_money to the index of the name you put in in the start in people 
            return print(people[name_enter])    # returns and prints the sum



# Withdrawing money from one of the accounts in the 'people' dictionary
def withdraw(name_enter):
            input_money = input("How much to Withdraw: ") # account_name looks for your input
            people[name_enter] -= int(input_money)  # Subtracts the number of money you put in in input_money to the index of the name you put in in the start in people 
            return print(people[name_enter])    # returns and prints the sum
                    
                    
                    
                    
# Listing all of the accounts in the dictionary 'people'
def list_accounts():    # for calling the print of 'people'
    print(people)   





# Transfering the money between accounts
def transfer(name_enter):   # start of the transfer function 'name_enter' goes back to the name you chose 
            recipient = input("Enter the name of the account to transfer to: ") # recipient looks for the input of the account you want to transfer 

            amount = int(input("Enter the amount to transfer: ")) # amount stores the number you put in and stores it as a 'int'

            if amount <= people[name_enter]:    # if amount is less than or equal to the number in the index of people that you selected:
                people[name_enter] -= amount    # then subtract from the first account... "or the account you selected" ... 
                people[recipient] += amount     # then add the money you want to the the recipient
                print(f"Transfered {amount} from {name_enter} to {recipient}")  # printing the varibles of what happened
                print(f"New balance for {name_enter}: {people[name_enter]}")    # ^^
                print(f"New balance for {recipient}: {people[recipient]}")      # ^^    # ngl these were annoying af

        



# Adding and Removing accounts 
def add_remove():
    add_or_remove_action = input("Would you like to Add or Remove an account? (A/R): ").lower() # add_or_remove_action asks for input for what the user wants to do
    # string lower for more convience sake



    if add_or_remove_action == 'a': # Adding a new account 'a'
                global new_account
                global initial_balance

                new_account = input("Enter the new account name: ") # new_account looking for input from user for the new name
                initial_balance = int(input("Enter the initial balance: ")) # varible for adding a new balance if pressed a for add
                people[new_account] = initial_balance   # then add to the people dict. above
                print(f"Account {new_account} added with balance {initial_balance}.")   # now print the new account and the blaance you put in



    elif add_or_remove_action == 'r':   # if the person wants to remove a account
                account_to_remove = input("Enter the account name to remove: ") 
                if account_to_remove in people: # if what you want to remove is in 'people'
                    del people[account_to_remove]   # del for deleting a person out of the people dict.
                    print(f"Account {account_to_remove} removed.")  # return this in a print



def read_write_txt():
    outfile = open("All_accounts_written.txt", "w")

    #outfile.write(new_account + "\n")
    #outfile.write(initial_balance + "\n")
    outfile.write(str(people))

    outfile.close













# Leaving the program
def leave_program(): # exiting the program function 
    check = True
    while(check == True):
        print("Would you like to leave the program?")
        desc = str(input("Yes or No?: "))       # varible for making a decision
        
        if desc.lower() == "yes":
            print("Exiting the program...")
            exit()  # Varible that kills the whole thing
        
        if desc == "no":
            print("Returning to main...")
            main()  # Goes back to main

        else:
            print("Wront input...")
            leave_program() # Re-runs the "leave_program" function again    
        
    
        
        

if __name__ == "__main__":
    main()
    leave_program()







"""
functions directly interact with the global people
make functions for everything
call them when selecting things


deposit(name_enter)
    withdraw(name_enter)
    list_accounts()
    transfer(name_enter)
    add_remove()
    leave_program()
    read and write txt()

    dont forget name_enter for like everythig 

    
The main loop calls the appropriate function based on the option selected by the user

functions directly interact with the global people hashmap

string literals (re explination)
https://stackoverflow.com/questions/57150426/what-is-printf
    The f or F in front of strings tell Python to look at the values , expressions or instance inside {} and substitute them with the variables values or results if exists

https://www.w3schools.com/python/ref_string_lower.asp

"""

#IGNORE:
#elif account_name in accounts:
            #amount = float(input("Enter amount you want to enter: "))
            #           amount = float(input("Enter amount to deposit: "))
        # elif option == 2: # Transfer
