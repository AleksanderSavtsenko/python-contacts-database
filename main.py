import json, os

path = (os.path.dirname(os.path.abspath(__file__)) + "\contacts.txt").replace("\\", "/")

def read():
    with open(path, encoding="utf-8") as file: 
        return json.loads(file.read())

def write(data):
    with open(path, mode="w", encoding="utf-8") as file: 
        file.write(json.dumps(data))

def show(data = None):
    if (data == None): data = read()

    if (len(data) == 0):
        print()
        print("There are no users in the database")
        return

    print()

    print("{:<8} {:<28} {:<8} {:<16} {:<32}".format('Id','Name','Age','Phone','Email'))
    
    for key, value in data.items():
        print("{:<8} {:<28} {:<8} {:<16} {:<32}".format(key, value["name"], value["age"], value["phone"], value["email"]))

def create():
    print()
    print("The procedure for adding a user to the database has been started. To cancel, leave any of the fields blank")

    name = input("Enter name: ")
    if (name == "" or name == None): return
    
    age = input("Enter age: ")
    while (True):
        if (age == "" or age == None): return
        try:
            age = int(age); break
        except ValueError:
            age = input("Incorrect input. Enter correct age: ")

    phone = input("Enter phone: ")
    if (phone == "" or phone == None): return

    email = input("Enter email: ")
    if (email == "" or email == None): return

    data = read()

    try:
        new_id = int(list(data)[-1]) + 1
        print(new_id)
    except:
        new_id = 1
        
    data[new_id] = {
        "name": name,
        "age": age,
        "phone": phone,
        "email": email,
    }
    
    write(data)
    print("Success")

def edit():
    print()
    print("User editing mode. To cancel, leave any of the fields blank")

    data = read()

    id = input("Enter the user ID to edit: ")
    while (True):
        if (id == "" or id == None): return

        try:
            id = int(id); break
        except ValueError:
            id = input("Incorrect input. Enter correct ID: ")

        if (not id in data):
            id = input("There is no user with this ID in the database. Enter the ID of an existing user: "); break

    def print_edit_menu():
        print()
        print("What do you want to do?")
        print("[1] Change name")
        print("[2] Change age")
        print("[3] Change phone")
        print("[4] Change email")
        print("[5] Remove user")
        print("[0] Return to the main menu")
        return input("Choose an action [0-5]: ")

    while (True):
        option = print_edit_menu()
        if (option == "0"):
            return
        elif (option == "1"):
            data[str(id)]["name"] = input("New name: ")
            write(data)
            print("Success")
        elif (option == "2"):
            age = input("New age: ")
            while (True):
                if (age == "" or age == None): return
                try:
                    age = int(age); break
                except ValueError:
                    age = input("Incorrect input. Enter correct age: ")
            data[str(id)]["age"] = age
            write(data)
            print("Success")
        elif (option == "3"):
            data[str(id)]["phone"] = input("New phone: ")
            write(data)
            print("Success")
        elif (option == "4"):
            data[str(id)]["email"] = input("New email: ")
            write(data)
            print("Success")
        elif (option == "5"):
            print()
            print("Are you sure of your actions?")
            print("[1] Yes")
            print("[0] Back")
            if (input("Choose an action [0/1]: ") == "1"): 
                del data[str(id)]
                write(data)
                return
            else: continue
        else:
            print()
            print("Choose correct one!")
    

def menu():
    print()
    print("You are in the main menu. Available commands:")
    print("[1] List users")
    print("[2] Edit / delete user")
    print("[3] Add user")
    print("[0] Exit")
    return input("Choose an action [0-3]: ")

def main():
    while (True):
        option = menu()
        if (option == "0"):
            print()
            quit()
        elif (option == "1"):
            show()
        elif (option == "2"):
            edit()
        elif (option == "3"):
            create()
        else:
            print()
            print("Choose correct one!")

main()
