class EmployeeData:
    def __init__(self, emp_id, emp_name, emp_age, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_salary = emp_salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.emp_name}, Age: {self.emp_age}, Salary: {self.emp_salary}"

def sort_employee_records(employees, sorting_parameter):
    if sorting_parameter == 1:
        employees.sort(key=lambda x: x.emp_age)
    elif sorting_parameter == 2:
        employees.sort(key=lambda x: x.emp_name)
    elif sorting_parameter == 3:
        employees.sort(key=lambda x: x.emp_salary)
    else:
        print("Invalid sorting parameter")
        return

    print("\nSorted Employee Data:")
    for emp in employees:
        print(emp)

if __name__ == "__main__":
    employee_records = [
        EmployeeData("161E90", "Raman", 41, 56000),
        EmployeeData("161F91", "Himadri", 38, 67500),
        EmployeeData("161F99", "Jaya", 51, 82100),
        EmployeeData("171E20", "Tejas", 30, 55000),
        EmployeeData("171G30", "Ajay", 45, 44000),
    ]

    print("Employee Table:")
    for emp in employee_records:
        print(emp)

    sorting_option = int(input("\nChoose a sorting parameter (1. Age, 2. Name, 3. Salary): "))
    sort_employee_records(employee_records, sorting_option)
