d1 = {
    101 : {'E101' : 50000,'E003' : 70000,'E007': 72000},
    102 : {'E102' : 60000,'E005' : 56000,'E008': 68000},
    103 : {'E104' : 55000,'E006' : 52000,'E007': 45000}
}
deptsalary = {}
for dept,employee in d1.items():
    salaries = list(employee.values())
    deptsalary[dept] = {
        "min salary" : min(salaries),
        "max salary" : max(salaries)
    }
for dept,summary in deptsalary.items():
    print(f"
