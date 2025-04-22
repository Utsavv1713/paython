
queue = []

def enqueue():
    item = input("Enter element to enqueue: ")
    queue.append(item)
    print(f"'{item}' has been added to the queue.")

def dequeue():
    if not queue:
        print("Queue is empty! Nothing to dequeue.")
    else:
        item = queue.pop(0)
        print(f"'{item}' has been removed from the queue.")

def display():
    if not queue:
        print("Queue is empty!")
    else:
        print("Current Queue:")
        print(" <- ".join(queue))


while True:
    print("\n=== Queue Operations Menu ===")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
