# Empty dictionary to hold all entries:
catalog = {}
program_stop = True


while program_stop == True:
    print("\n Electronic Phone Book \n")
    print("======================")
    print("\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
    user_input = int(input("What do you want to do? Pick a number from 1 -5: "))
    #Look up an Entry:
    if (user_input == 1):
        name_selection = input("Who would you like to look up? ")
        if (name_selection == catalog["user_name"]):
            print(catalog["user_name"] + " " + catalog["user_number"])
        else:
            print("Sorry, we don't have someone with that name in our database.")
    # Set an Entry:
    if (user_input == 2):
        user_name = input("Enter your name: ")
        user_number = input("Enter your phone number: ")
        catalog["user_name"] = user_name
        catalog["user_number"] = user_number
        print("You have added an entry for %s with the phone number: %s." % (catalog["user_name"], catalog["user_number"]))
    #Delete an Entry:
    if (user_input == 3):
        print(catalog)
        entry_to_delete = input("Whose entry would you like to delete? ")
        if entry_to_delete == catalog["user_name"]:
            del catalog["user_name"]
            print("The entry has been deleted.")
        else:
            print("We don't have anyone with that name in our database.")
    # List all Entries:
    if (user_input == 4):
        print(catalog)
    #Quit the Program:
    if (user_input == 5):
        print("See you next time!")
        program_stop = False
        