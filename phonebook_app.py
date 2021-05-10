#Create a dictionary that can store entries and output that information to the user. 

# Empty dictionary to hold all entries:
catalog = {
    "bob": "123-455-9678",
    "judie": "444-301-5497"
    
}
program_stop = True

#Note 5/10 This could just be changed to while program_stop, the == true is just an extra step.
while program_stop == True:
    print("\n Electronic Phone Book \n")
    print("======================")
    print("\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
    user_input = int(input("What do you want to do? Pick a number from 1 -5: "))
    
    #Look up an Entry:
    if (user_input == 1):
        name_selection = input("Who would you like to look up? ")
        lower_case_name = name_selection.lower()
        if lower_case_name in catalog:
            #.capitalize capitalizes the first letter
            print(name_selection.capitalize() + "'s phone number is: " + catalog[lower_case_name]) 
        else:
            print("Sorry, we don't have someone with that name in our database.")
            
    # Set an Entry:
    if (user_input == 2):
        user_name = input("Enter your name: ")
        user_number = input("Enter your phone number: ")
        lower_case_name = user_name.lower()
        catalog[lower_case_name] = user_number
        print("You have added an entry for " + user_name + ".")
        
    #Delete an Entry:
    if (user_input == 3):
        print(catalog)
        entry_to_delete = input("Whose entry would you like to delete? ")
        lower_entry_to_delete = entry_to_delete.lower()
        if lower_entry_to_delete in catalog:
            del catalog[lower_entry_to_delete]
            print("The entry for " + lower_entry_to_delete + " has been deleted.")
        else:
            print("We don't have anyone with that name in our database.")
            
    # List all Entries:
    if (user_input == 4):
        for contact in catalog:
            print("Found an entry for " + contact.capitalize() + ": " + catalog[contact])
        
    #Quit the Program:
    if (user_input == 5):
        print("See you next time!")
        program_stop = False

        