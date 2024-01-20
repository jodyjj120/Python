class Employee :

    def __init__(self, name, age, salary, gender):


        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender


    def Employee_details(self) :
        print("name of the employee is :", self.name)
        print("age of the employee is :", self.age)
        print("salary of the employee is :", self.salary)
        print("gender of the employee is :", self.gender)


e1 = Employee("rajat", 48, 48000, "male")

e1.Employee_details()

