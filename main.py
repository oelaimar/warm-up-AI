import os

EXIT = False

RESET   = "\033[0m"

BOLD    = "\033[1m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"

# clear the terminal on windows (nt) system and unix-like system (posix)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_contacts():
    if not os.path.exists("contacts.txt"):
        return []
    
    contacts = []
    with open("contacts.txt", "r") as file:
        for line in file:
            contacts.append(eval(line))
        return contacts
    
def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(repr(contact) + "\n")
    
contacts = get_contacts()

last_id = contacts[-1]["id"] if contacts else 0


def pause():
    input(MAGENTA + "Click Enter to continue ...." + RESET)
    
    
def add_contact():
    global last_id
    name = input(CYAN + "Enter contact name: " + RESET)
    phone = input(CYAN + "Enter phone number: " + RESET)
    email = input(CYAN + "Enter email address: " + RESET)
    
    if not name:
        print(RED + "name cannot be empty" + RESET)
    if not phone:
        print(RED + "phone cannot be empty" + RESET)
    if not email:
        print(RED + "email cannot be empty" + RESET)
    if not name or not phone or not email:
        return

    last_id += 1
    
    contacts.append({"id" : last_id ,"name" : name, "phone" : phone, "email" : email})
    print(f"{GREEN}The Contact {name} added successfully{RESET}")
    
def display_contacts():
    if len(contacts) <= 0 :
        print(RED + "No contacts found." + RESET)
        return
    print(BLUE + "============= CONTACTS =============" + RESET)
    
    for contact in contacts:
        print(f"{GREEN}id    :{RESET} {contact["id"]}")
        print(f"{GREEN}name  :{RESET} {contact["name"]}")
        print(f"{GREEN}phone :{RESET} {contact["phone"]}")
        print(f"{GREEN}email :{RESET} {contact["email"]}")
        print(BLUE + "====================================" + RESET)
        
def delete_by_id():

    display_contacts()
    
    if len(contacts) <= 0 :
        return
    
    try:
        id = int(input(YELLOW + "Choose the ID of the contact you want to delete: " + RESET))
    except ValueError:
        print(RED + "Please enter a valid ID." + RESET)
        return
    
    for contact in contacts:
        if int(contact["id"]) == int(id):
            deleted_contact = contact
            contacts.remove(contact)
            print(f"{GREEN}Contact {deleted_contact["name"]} deleted successfully!{RESET}")
            return
    print(RED + "Please enter a valid ID." + RESET)

while not EXIT:
    clear()
    
    print(BOLD + CYAN + "======== CONTACTS MANAGER ========" + RESET)
    print(BLUE + "\t1." + RESET + "add contact: ")
    print(BLUE + "\t2." + RESET + "display contact: ")
    print(BLUE + "\t3." + RESET + "delete contact: ")
    print(BLUE + "\t0." + RESET + " exit: ")
    
    choice = input(YELLOW + "Choose your operation: " + RESET)
      
    match choice:
        case '1':
            clear()
            add_contact()
            save_contacts()
            pause()
        case '2':
            clear()
            display_contacts()
            pause()
        case '3':
            clear()
            delete_by_id()
            save_contacts()
            pause()
        case '0':
            clear()
            print(CYAN + "Exiting Contact Manager... Goodbye!" + RESET)
            EXIT = True
        case _ :
            print(RED + "Invalid option. Please try again." + RESET)
            pause()