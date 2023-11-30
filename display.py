dish = str(input("Enter the item:"))
price = str(input("Enter price:"))

menu = dish + price

total = len(menu)


dots = "."*(25-total)

print(dish+dots+price)