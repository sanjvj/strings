original = input("Enter a string:")

rev = original[::-1]

print("Reverse of the string is:",rev)

if original == rev:
    print("Yes it is a palindrome")
    
else:
    print("No it is not a palindrome")
    y = input("Do you want to see the palindrome? Y/N:")
    if y=='Y':
        palindrome_original = original+rev
        palindrome_rev = palindrome_original[::-1]
        
        print(palindrome_rev)
    else:
        print("Thank youu")      



#To change a string to palindrome

