# Smart Login System with Security Rules

# Predefined correct credentials
correct_username = "admin123"
correct_password = "pass@123"
account_active = True   # Change to False to test disabled account

# Taking user input
username = input("Enter username: ")
password = input("Enter password: ")

# Login validation using short-circuit logic
if username == correct_username and password == correct_password and account_active:
    print("Login Successful")

elif username == correct_username and password == correct_password and not account_active:
    print("Account Disabled")

else:
    print("Wrong Credentials")
