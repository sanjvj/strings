email = input("Enter your email id: ")

middle = email.rfind("@")

userId = email[0:middle]
domain = email[middle+1:]

print("Your user ID is :",userId)
print("Your domain name is:",domain)