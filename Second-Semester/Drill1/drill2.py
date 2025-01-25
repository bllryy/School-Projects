def main():
    sentence_input = input("input ur sentence: ")  
    empty_string = "" 
    words = sentence_input.split()  

    
    for word in reversed(words):
        empty_string += word + " "  

    print(empty_string.strip())  

if __name__ == "__main__":
    main()
