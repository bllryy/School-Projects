""" 
Name:
Section:
Description: Lab 4 
"""



"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    # refactor INTO A WHILE LOOP 

    list_of_nums = []

    users_input_for_list = int(input("Enter the number of elements: "))

    for i in range(users_input_for_list):
        element = int(input(f"Enter element: "))  # Ensure input is numeric
        list_of_nums.append(element)

    print("List:", list_of_nums)
    return list_of_nums



""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("\nStatistics Calculator Menu:")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Find Minimum")
    print("4. Find Maximum")
    print("5. Empty List")
    print("6. Exit")


"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(users_input_for_list):
    return sum(users_input_for_list) / len(users_input_for_list) 


"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(users_input_for_list):
    # sort the List
    userList = sorted(userList)
    mid = len(userList) // 2
    
    if len(userList) % 2 == 0:
        return (userList[mid - 1] + userList[mid]) / 2
    else:
        return userList[mid]


""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(users_input_for_list):
    return min(users_input_for_list)

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(users_input_for_list):
  return max(users_input_for_list) 

""" 
Function Name: emptyList
Parameters: none
Return Type: none
Description: Empties out the list of numbers
"""
def emptyList():
    print("The list has been emptied.")
    return []



def main():
    user_input = getList()
    while True:
        printMenu()
        user_choice = input("Enter a choice between 1-6: ")

        if user_choice == "1":
            mean = getMean(user_input)
            if mean is not None:
                    print("Mean", mean)

        if user_choice == "2":
        # median 
            median = getMean(user_input)
            if median is not None:
                print("Median", median)

        if user_choice == "3":
        # minimum
            minimum = getMin(user_input)
            if minimum is not None:
                print("Minimum", minimum)
        if user_choice == "4":
        # maximum
            maximum = getMax(user_input)
            if maximum is not None:
                print("Maximum", maximum)
        
        if user_choice == "5":
        # empty the list 
            empty_list = emptyList(user_input)
            if empty_list is not None:
                print("Empty List", empty_list)


if __name__ == "__main__":
    main()
