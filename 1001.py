import csv

# Create a CSV file
with open("students.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["RollNo", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([101, "Alice", 80, 90, 85])
    writer.writerow([102, "Bob", 70, 75, 80])
    writer.writerow([103, "Charlie", 88, 92, 86])
