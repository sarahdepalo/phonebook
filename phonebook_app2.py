#Use functions to make the phonebook_app cleaner.
catalog = {
    "bob": "123-455-9678",
    "judie": "444-301-5497"
    
}

program_stop = True

def option1():
    name_selection = input("Who would you like to look up? ")
    lower_case_name = name_selection.lower()
    if lower_case_name in catalog:
        print(name_selection.capitalize() + "'s phone number is: " + catalog[lower_case_name]) 
    else:
        print("Sorry, we don't have someone with that name in our database.")

def option2():
    user_name = input("Enter your name: ")
    user_number = input("Enter your phone number: ")
    lower_case_name = user_name.lower()
    catalog[lower_case_name] = user_number
    print("You have added an entry for " + user_name + ".")

def option3():
    print(catalog)
    entry_to_delete = input("Whose entry would you like to delete? ")
    lower_entry_to_delete = entry_to_delete.lower()
    if lower_entry_to_delete in catalog:
        del catalog[lower_entry_to_delete]
        print("The entry for " + lower_entry_to_delete + " has been deleted.")
    else:
        print("We don't have anyone with that name in our database.")

def option4():
    for contact in catalog:
        print("Found an entry for " + contact.capitalize() + ": " + catalog[contact])

def option5():
    print("See you next time!")

while program_stop:
    print("\n Electronic Phone Book \n")
    print("======================")
    print("\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
    user_input = int(input("What do you want to do? Pick a number from 1 -5: "))
    if user_input == 1:
        option1()
    elif user_input == 2:
        option2()
    elif user_input == 3:
        option3()
    elif user_input == 4:
        option4()
    elif user_input == 5:
        option5()
        program_stop = False
    else:
        print("Please select an option using a number 1 -5.")
    
