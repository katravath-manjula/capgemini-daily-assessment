from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self) -> str:
        pass

    @abstractmethod
    def get_salary(self) -> float:
        pass

# Concrete Employee Classes
class Manager(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)
    
    def work(self) -> str:
        print(f"{self.name} is managing the team.")
    
    def get_salary(self) -> float:
        print(self.salary)

class Developer(Employee):
    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)
    
    def work(self) -> str:
        print(f"{self.name} is writing code.")
    
    def get_salary(self) -> float:
        print(self.salary)

# Department Class to Manage Employees
class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
    
    def hire(self, employee: Employee):
        self.employees.append(employee)
    
    def fire(self, employee: Employee):
        self.employees.remove(employee)
    
    def get_total_salary(self) -> float:
        return sum(emp.salary for emp in self.employees)
    
    def show_employee_details(self):
        for emp in self.employees:
            emp.work()
            emp.get_salary()

# Testing the Implementation
if __name__ == "__main__":
    dev1 = Developer("Alice", 50000)
    dev2 = Developer("Bob", 45000)
    mgr1 = Manager("Charlie", 70000)
    
    dept = Department("Software Engineering")
    dept.hire(dev1)
    dept.hire(dev2)
    dept.hire(mgr1)
    
    print("Employee Details:")
    dept.show_employee_details()
    print(f"Total Salary Expense: {dept.get_total_salary()}")
