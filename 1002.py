students = {}
with open("students.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        total = sum(int(row[f'Subject{i}']) for i in range(1, 4))
        students[row["RollNo"]] = {
            "Name": row["Name"],
            "Marks": [int(row["Subject1"]), int(row["Subject2"]), int(row["Subject3"])],
            "Total": total
        }

# Display
for roll, data in students.items():
    print(f"Roll No: {roll}, Name: {data['Name']}, Marks: {data['Marks']}, Total: {data['Total']}")