"""
Name: Fin Goscha
Section: 275-02
Desc: Lab3

"""



usr_string = input("Please input your word: ")
usr_string = usr_string.lower() # lowercase the string

palidrome = ''

i = len(usr_string) -1 # sets the index to the end of the string
for char in usr_string: # for characters in the user given string
    palidrome += char # builds the revers string
    i -= 1  # reduces 'i' in each loop iteration

print(usr_string) # user input
print(palidrome) # and the new word

if usr_string in palidrome: # if it is a palidrome or not
    print("is palidrome")
else:
    print("not palidrome")

~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~              