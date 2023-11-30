s1 = input("Enter first word:")
s2 = input("Enter second word:")

new_s1 = sorted(s1)
new_s2 = sorted(s2)

if new_s1 == new_s2:
    print("yes it is anagram")
else:
    print("it is not")