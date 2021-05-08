# Adding user input to a dictionary.

#Create an empty dictionary

phonebook = {}

#Set a flag
program_close = True

while program_close == True:
    username = input("\n What's your name? ")
    user_number = input("What is your phone number? ")
    #Store responses in a dictionary
    phonebook[username] = user_number
    print(phonebook)
    print("You have succesfully added an entry for the number: %s." % (phonebook[username]))
    program_close = False
