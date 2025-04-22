menu = [("Burger", 99), ("Pizza", 150), ("Fries", 60), ("Pasta", 120)]

sorted_menu = sorted(menu, key=lambda x: x[1], reverse=True)
print("Menu sorted by price (descending):")
print(sorted_menu)
