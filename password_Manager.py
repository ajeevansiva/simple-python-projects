mast_pwd = input("What is your master password? ")


def view():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password:",passw)


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open("password.txt",'a') as f:
        f.write(name + " | " + pwd + "\n")



while True:
    mode = input("Would you like to add a new password or view existing one? (view/add)\nor type q to quit : ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")
        continue
