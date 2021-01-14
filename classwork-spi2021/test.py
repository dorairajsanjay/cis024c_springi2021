import random

# initializing employees
employees = []

for i in range(5):
    employee = []
    employee.append(i)
    employee.append("name-" + str(i))
    employee.append(int(10000 * random.random()))
    
    # populate the list
    employees.append(employee)

emp_id = int(input("Enter an employee_id to search:"))

for employee in employees:
    
    if employee[0] == emp_id:
        print("Found employee:",employee)
        break

