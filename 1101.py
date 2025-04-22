def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            print(f"You entered the integer: {num}")
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")
            
get_integer()
