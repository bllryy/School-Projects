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



def converttonum(message):
    """
        Convert's a plaintext message to a list of its corresponding ASCII values
        
    Args:
        message (_string_): Message that will be converted to list of numbers
    Return:
        converted (_List_): List of ASCII values corresponding to the characters in message
    """

    ascii_the_values = ord(char) 
    for char in message:
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


def vigenereEncrypt(plaintext,key):
    """Encrypts plaintext by Vigenere Cipher.

    Args:
        plaintext (List): List of ASCII Values for plainText
        key (List): List of ASCII Values for key
        
    Returns:
        List: List of ASCII VAlues for ciphertext
    """
    encrypted = []
    for i in range(len(plaintext)):
        encrypted.append((plaintext[i] + key[i]) % 256)
    print("encrypted value", encrypted)


def vigenereDecrypt(Ciphertext,key):
    """Decrypts Ciphertext by Vigenere Cipher.

    Args:
        Ciphertext (List): List of ASCII Values for CipherText
        key (List): List of ASCII Values for key
        
    Returns:
        List: List of ASCII VAlues for Plaintext
    """
    plaintext = []
    for i in range(len(Ciphertext)):
        plaintext.append((Ciphertext[i] - key[i]) % 256)
    return plaintext

def RSA(message, p, q, encry, decry):
    """RSA Encryption Scheme: Allows for choice between encrypting or decrypting depending on if the user chooses the original exponent or the modular inverse.

    Args:
        message (String): Plaintext or Ciphertext
        p (Integer): First Prime Number
        q (Integer): Second Prime Number
    """
    
    euler = (p -1) * (q-1)

    if encry is not 0: #TODO fix later
        ciphertext = []
    for char in message:
        ascii_value = ord(char) # Convert character to ASCII
    encrypted_char = fast_mod_exp(ascii_value, encry) # Encrypt using fast modular exponentiation
    ciphertext.append(encrypted_char) # Append the encrypted character to the ciphertext list
    encry = 0

    elif decry is not 0:
    plaintext = []
    for char in message:
        decrypted_char = fast_mod_exp(message) # TODO FIX
        plaintext.append(chr(decrypted_char)) # Convert the decrypted value back to a character
    plaintext_message = ''.join(plaintext) # Join the decrypted characters into a single string TODO DELETE
    print("Decrypted message:", plaintext_message)
    return plaintext_message; decry = 0
    



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
            message = input("Enter the message: ")
            key = int(input("Enter the shift key: "))
            ascii_values = converttonum(message)
            shifted_values = shift(ascii_values, key)
            print("Shifted text:", converttotext(shifted_values))

        elif option == 2:
            message = input("Enter the message: ")
            key = input("Enter the key: ")
            extended_key = generate_key(message, key)
            print("Extended Key:", extended_key)
            
        elif option == 3:
            message = input("Enter the message (or ciphertext for decryption): ")
            p = int(input("first prime number (p): "))
            q = int(input("second prime number (q): "))
            encry = int(input("num for encryption or leave empty for decryption: "))

            if encry > 0:
                RSA(message, p, q, e = encry)  # encrypt
            else:
                decry = int(input("Enter private exponent (d) for decryption: "))
                RSA(message, p, q, d = decry)  # decrypt


        elif option == 4:
            check = False
            
            
            
if __name__ == "__main__":
    main()
