def main():

    sentence_input = (input(str("Insert your sentece : ")))
    empty_string = ""
    words = sentence_input.split()

    for word in words:
        empty_string = empty_string + word 
        for i in range(len(word)):
            empty_string = empty_string + "_"
    print(empty_string)



if __name__ == "__main__":
    main()
