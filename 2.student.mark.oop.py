class Number:
    def numb (self):
        self.numbstu = input("Number of student in class: ")
        self.numbcource = input("Number of cource: ")
    def print(self):
        print(self.numbstu, self.numbcource)

N1 = Number()
N1.numb()
print("Number of student and cource: ")
N1.print()

class Information:
    def __init__(self, n, i, d):
        self.name = n
        self.id = i
        self.dob = d

    def describe(self):
        print("Name: ", self.name)
        print("Id: ", self.id)
        print("Date of birth: ", self.dob)

    def __str__(self):
        return f"Name is: {self.name}, ID is: {self.id} and DoB is: {self.dob}"

class Student(Information):
    def set_term(self, term):
        print(f"Setting term to{term}")
        self.term = term

class Cource:
    def math(self):
        print("Math mark is: ")

    def work(self):
        print("um")

    def __init__(self):
        self.__point = 0

    def _get_point(self):
        return self.__point

    def set_point(self, point):
        self.__point = point

    def work(self):
        if self.__point < 5 :
            print("Not good")
        else:
            print("Good")
    
class Student(Information, Cource):
    def describe(self):
        super().describe()
        print("Term:", self.term)

    def work(self):
        super().work()









macron = Information("Emmanuel Macron",100, 24.12)
print(macron)
macron = Student
macron.set_term(25)
macron.describe()
macron.set_point(10)
macron.math(8)


biden = Information("Joe Biden",101)
print(biden)