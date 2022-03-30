#Inheritance
#parent class # inherit, extend and override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ....")


class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):     #overriding parent class
        #calling the initializer of the parent class
        super().__init__(name, age, salary)
        self.level = level   #extending parent class

    def debug(self):
        print(f"{self.name} is debugging ....")

    def work(self):                            #overriding parent class
        print(f"{self.name} is coding ....")


class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing ....")

    def work(self):                           #overriding parent class
        print(f"{self.name} is designing....")


#instance
se = SoftwareEngineer("Ama", 25, 7000, "Junior")
#print(se.name, se.age)
#se.work()
#print(se.level)
#se.debug()
'''''

'''''
d = Designer("Glen", 27, 8000)
#print(d.name, d.age)
#d.work()
#d.draw()


#Polymorphism

employee = [SoftwareEngineer("Ama", 25, 7000, "Junior"), SoftwareEngineer("Kwaku", 29, 9000, "Senior"),
            Designer("Glen", 27, 8000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employee)



