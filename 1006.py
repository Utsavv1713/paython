import pickle

# Employee class
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"Code: {self.empcode}, Name: {self.empname}, DOJ: {self.doj}, Salary: {self.salary}"

# Serialize
emp = Employee(1, "Alice", "2021-01-10", 60000)
with open("employee.dat", "wb") as f:
    pickle.dump(emp, f)
print("Employee object serialized.")

# Deserialize
with open("employee.dat", "rb") as f:
    loaded_emp = pickle.load(f)
    print("Deserialized Employee:")
    print(loaded_emp)
