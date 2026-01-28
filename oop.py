import numpy
class Employee:
    raise_amount = 1.04
    no_of_employees = 0
    def __init__(self, name, email, salary):
        Employee.no_of_employees+=1
        self.name = name
        self.email = email
        self.salary = salary

    def print_obj(self):
        print(f"Name : {self.name}\nEmail : {self.email}\nsalary : {self.salary}\n")
    
    def apply_raise(self):
        self.salary = self.salary*Employee.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_working(day):
        if day.lower() == 'saturday' or day.lower() == 'sunday' : 
            return False
        return True

    def __str__(self):  # for end user, less detailed information
        return f"( {self.name}, {self.email}, {self.salary})"

    def __repr__(self): # for developer, more detailed information
        return f"Employee( {self.name}, {self.email}, {self.salary})"

    def __delete__(self):
        print("Instance is deleted!!!")

class Developer(Employee):
    raise_amount = 1.05
    def __init__(self, name, email, salary, programming_lang):
        super().__init__(name, email, salary)
        self.programming_lang = programming_lang

class Manager(Employee):
    def __init__(self, name, email, salary, employees=None):
        super().__init__(name, email, salary)
        self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp) 
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employess(self):
        for emp in self.employees:
            print(emp, end = " ")


# print(f"Total employees : {Employee.no_of_employees}")
# emp1 = Employee('Ajay', 'ajay@gmail.com', 3000000)
emp2 = Employee('test user', 'testuser@gmail.com', 20000000)
# print(emp2)
print(str(emp2))
print(repr(emp2))

# print(f"Total employees : {Employee.no_of_employees}")
# print(type(emp1))
# emp1.print_obj()
# Employee.print_obj(emp1)

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# emp1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp1.raise_amount)

# name = "Test-User"
# fname, lname = name.split("-")
# print(fname, lname)
# Employee.set_raise_amount(1.05)
# print(Employee.is_working('Sunday'))

# dev1 = Developer('Test', 'test@gmai.com', 1000000, ['C++', 'Python'])
# mng_1 = Manager("test_manager", "manager@gmail.com", 1230000, ['emp1', 'emp2'])
# mng_1.print_employess()
# print(dev1.programming_lang)
# print(help(Developer))  #Method resolution order

# dev1.apply_raise()
# print(dev1.salary)
# dev1.raise_amount = 1.06
# print(Employee.raise_amount)
# print(Developer.raise_amount)

# print(isinstance(dev1, Developer))
# print(issubclass(Developer, Employee))