credit = input("Enter your credit card number:")[:19]

last = credit[-4:]

display = ('*'*4 + ' ')*3 + last
print(display)