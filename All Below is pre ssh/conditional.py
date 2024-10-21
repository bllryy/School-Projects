"""
Name: ---------- (cause its on github ( ͡° ͜ʖ ͡°))
Section: 275-02
Desc: Lab2
"""


def main():
    check = True
    while(check == True):
        print("What op do you watn to do????")
        print("1. add")
        print("2. sub")
        print("3. multiply")
        print("4. divide")
        print("5. quti")
        option = int(input("enter your option: ")) # prompt - user for input of operation
        if option == 1:
            var1 = int(input("Enter your first number: ")) # var1 for adding
            var2 = int(input("Enter your second number: ")) # var2 for adding
            sum = var1 + var2                                                           # sum of var1 +  var2
            print("your result is: " + str(sum)) 
        elif option == 2: 
            var1 = int(input("Enter your first number: "))  #v1 for sub
            var2 = int(input("Enter your second number: ")) #v2 for sub
            sum = var1 - var2                                                           # sum of "-"
            print("your result is: " + str(sum)) 
        elif option == 3: 
            var1 = int(input("Enter your first number: "))  #v1 for mult 
            var2 = int(input("Enter your second number: ")) #v2 for multi
            sum = var1 * var2                                                           # sum of multi
            print("your result is: " + str(sum)) 
        elif option == 4: 
            var1 = int(input("Enter your first number: ")) #v1 for divide
            var2 = int(input("Enter your second number: ")) #v2 for divide
            sum = var1 / var2                                                               # sum of divide
            print("your result is: " + str(sum)) 
        elif option == 5: 
            check = False
    


# need for full credit
if __name__ == "__main__":
    main()

    """
      print(check)
        var1 = int(input("input var 1 "))
        if var1 == 5:
            check = False
    """