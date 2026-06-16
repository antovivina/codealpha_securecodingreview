

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Login Successful")
else:
    print("Login Failed")

query = "SELECT * FROM users WHERE username = '" + username + "'"
print("Generated Query:", query)