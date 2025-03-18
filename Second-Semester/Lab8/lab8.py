def fast_mod_exp(b, exp, m):
    """
    TO BE USED IN RSA 
    """
    res = 1
    while exp > 1:
        if exp & 1:
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1
    return (b * res) % m


def gcd(a, b):
    """
    TO BE USED IN RSA 
    """
    if b == 0:
        return a
    return gcd(b, a % b)

def modInverse(A, M):
    """
    TO BE USED IN RSA 
    """
    if gcd(A, M) > 1:
      
        # modulo inverse does not exist
        return -1
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def totient(p,q):
    """
        Euler's Totient Function. Takes in two prime numbers, P and Q, and computes the product (p-1)*(q-1). Used in RSA encryption scheme.
        
    Args:
        p (_int_): Integer 1 that is a prime number
        q (_int_): Integer 2 that is a prime number
    Return:
        result of (p-1)*(q-1)
    """
    return (p - 1) * (q - 1)

p = int(input("Please input a prime number (p): "))
q = int(input("Please input a prime number (q): "))

print("The result of Euler's Totient Function is:", totient(p, q))


pass


def converttonum(message):
    """
        Convert's a plaintext message to a list of its corresponding ASCII values
        
    Args:
        message (_string_): Message that will be converted to list of numbers
    Return:
        converted (_List_): List of ASCII values corresponding to the characters in message
    """

    input_string = input("Input the Text to convert Here: ")
    ascii_the_values = [ord(char) for char in input_string]
    print("ASCII Values:", ascii_the_values)



    pass
    
def converttotext(message):
    """Converts List of ASCII values to a String.

    Args:
        message (_List_): List of ASCII Values to be converted to a string
        
    Return: 
        Converted (_string_): Converted message
    """

    ascii_input = input("Enter ascii values with spaces: ")
    ascii_values = [int(num) for num in ascii_input.split()]  #  list of integers
    text = ''.join(chr(num) for num in ascii_values)  # convert to char #TODO fixlater
    print("Converted text:", text)


    pass


def shift(message,key):
    """Performs Shift Cipher on LIST of ASCII Values

    Args:
        message (List): List of ASCII Values
        key (Integer: Integer that you are shifting message by

    Returns:
        List: Shifted List of ASCII Values
    """
    # input for ASCII values
    ascii_values = list(map(int, input("Enter ASCII values separated by spaces (live above): ").split()))
    key = int(input("enter the shift key: "))

    # shift and display result
    shifted_values = shift(ascii_values, key)
    text = ''.join(chr(value) for value in shifted_values)
    print("new text:", text)
    
    pass

def generate_key(message, key):


    """Generates Extended Key (if needed) for Vigenere Cipher

    Args:
        message (String): String of Original Message
        key (String): String of Original Key

    Returns:
        String: Extended (or original) Key
    """
    message = input("Please enter the key: ")
    key = message

    for i in range(len(message)):
        key += len(key) + message
    
    print(key) 


def main():
    check = True
    while check:
        print("Welcome to the encryption calculator!")
        print("1. Shift Cipher")
        print("2. Vigenere Cipher")
        print("3. RSA Encryption")
        print("4. Quit")
        option  = int(input("Choose which Encryption Scheme you would like to use: "))

        if option == 1:
            ascii_values = list(map(int, input("Enter ASCII values separated by spaces: ").split()))
            key = int(input("Enter the shift key: "))
            shifted_values = shift(ascii_values, key)
            #print("Shifted text:", ''.join(chr(value) for value in shifted_values))

            pass
        elif option == 2:
            message = input("Enter the message: ")
            key = input("Enter the key: ")
            key_for_print = generate_key(message, key)
            print("Extended Key:", key_for_print)
            
        elif option == 3:
            print("Idk what to put here")
            pass
        elif option == 4:
            check = False
            
            
            
if __name__ == "__main__":
    main()
