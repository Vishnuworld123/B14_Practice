def login_system():
    # Sample users stored in a dictionary
    users = {
        "admin": "admin123",
        "user1": "pass1",
        "aish": "1234"
    }

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid username or password!")
        return False



