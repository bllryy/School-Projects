"""
Name: github
Section: 02
Description: Functions: List Exercise
"""




"""
Function Name: main 
Parameters: range(10) function 
Description: for loop to get a range of users input
Return Type: none
"""
def main():
    for numbers in range(10):  
        printGreeting()


"""
Function Name: printGreeting
Parameters: none
Description: Users input into if statement and isEven function to check if the numbers input is even or odd
Return Type: none
"""
def printGreeting():
    numbers = int(input("Enter a number to check if it is even or odd: "))
    if isEven(numbers):
        print(f"{numbers} is even")
    else:
        print(f"{numbers} is odd")



"""
Function Name: isEven
Parameters: value
Description: checks if the number is even or odd.
Return Type: bool - weather it is even or odd 
"""
def isEven(value):
    return value % 2 == 0


if __name__ == "__main__":
    main()

