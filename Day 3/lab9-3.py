for i in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == 'shahid011' and password == 'mynameiskhan':
        print("Logged in Successfully")
        break
    else:
        print("Invalid credentials!!")
    print("Try again!")
else:
    print("Attempts finished!!")


  