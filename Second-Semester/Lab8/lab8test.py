#input_string = input("Input the Text Here: ")
#ascii_the_values = [ord(char) for char in input_string]
#print("ASCII Values:", ascii_the_values)#

#input_ascii_values = input("Input the ascii to convert Here: ")
#string_the_values = [ord(ascii) for ascii in input_ascii_values]
#print("ASCII Values:", string_the_values)


#ascii_input = input("Enter ascii values with spaces: ")
#ascii_values = [int(num) for num in ascii_input.split()]  #  list of integers
#text = (chr(num) for num in ascii_values)  # cchar  
#print("Converted text:", text)
#



#ascii_values = list(map(int, input("Enter ASCII values separated by spaces (live above): ").split()))
#key = int(input("Enter the shift key: "))

    # shift and display result
#shifted_values = shift(ascii_values, key)
#text = ''.join(chr(value) for value in shifted_values)
#print("Converted text:", text)


#def shift(message, key):
#
#    shifted_message = [(char + key) % 256 for char in message]
#    return shifted_message
#
## User input for ASCII values
#ascii_values = list(map(int, input("Enter ASCII values separated by spaces: ").split()))
#key = int(input("Enter the shift key: "))
#
## Perform shift and display result
#shifted_values = shift(ascii_values, key)
#text = ''.join(chr(value) for value in shifted_values)
#print("Converted text:", text)
    
message = input("Please enter the key: ")
key = message

for i in range(len(message)):
    key += (len(key) + message)   
print(key)
