pass1 = input("Enter the password:")
pass2 = input("Re-enter your password:")

if pass1==pass2:
    print("Password created successfully")
    
elif pass1.upper() == pass2.upper():
    print("Please check your case and correct")
    
else:
    print("Enter password correctly")