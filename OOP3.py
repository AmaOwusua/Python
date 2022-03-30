#Encapsulation and Abstraction

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None             #private attributes(__) / protected attributes(_)
        self._num_bugs_solved = 0

    #getter @property(decorator)

    def get_salary(self):
        return self._salary

    #setter @salary.setter   /@salary.deleter

    def set_salary(self, value):
        self._salary = value


se = SoftwareEngineer("Max", 25)
print(se.age, se.name)

se.set_salary(6000)
print(se.get_salary())
