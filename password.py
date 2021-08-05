import random
passwords = {}
while True:
    choice = input("Would you like to make a password, access yours, or leave? (make/access/leave): ")
    
    if choice == "make":
        symbols = ["@", "!", "#", "$", "%", "^", "&", "*", "(", ")"]
        website = input("Website: ")
        first = input("Pick an animal: ")
        second = input("Pick 4 numbers: ")
        third = input("Pick a color: ")
        password = first.title() + random.choice(symbols) + second + random.choice(symbols) + third.title()
        website = website.title()
        pword = {website:password}
        passwords.update(pword)
        print(password)
    elif choice == "access":
        print(passwords)
    elif choice == "leave":
        break
    else:
        print("Please pick a valid option.")
        
    