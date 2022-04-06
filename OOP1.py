# position, name, age, level, salary

se1 = ["Software Engineer", "Ama", 25, "Junior", 6000]
se2 = ["Software Engineer", "Glen", 27, "Senior", 8000]
d1 = ["Designer", "Kwaku", 29, "Pro", 9000]

# creating a class


class SoftwareEngineer1:                   #renamed branch
    # class attribute

    alias = "Magician"

    def __init__(self, name, age, level, salary):      # (self) used to initialise parameters of the class
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

        #instance method

    def code(self):
        print(f"{self.name} is writing code ....")
#dunder method

    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level} "
        return information


# instance
se1 = SoftwareEngineer1("Ama", 25, "Junior", 6000)
print(se1.salary, se1.name)
se1a = se1.level
print(se1a)
print(se1.alias)
print(SoftwareEngineer1.alias)
se2 = SoftwareEngineer1("Glen", 27, "Senior", 8000)
print(SoftwareEngineer1.alias)

se1.code()
print(se1)

