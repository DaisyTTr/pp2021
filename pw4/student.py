class Number:
    def numb (self):
        self.numbstu = input("Number of student in class: ")
        self.numbcource = input("Number of cource: ")

    def getnumbcource(self):
        return self.numbcource

    def print(self):
        print(self.numbstu, self.numbcource)

N1 = Number()
N1.numb()
print("Number of student and cource: ")
N1.print()
class Student:
    def __init__(self, sn, si, sd):
        self.name = sn
        self.id = si
        self.dob = sd

    def get_sn(self):
        return self.name

    def get_si(self):
        return self.id
    
    def get_sd(self):
        return self.dob

    def describe(self):
        print("Student Name: ", self.name)
        print("Student Id: ", self.id)
        print("Student's Date of birth: ", self.dob)

    def __str__(self):
        return f"Student Name is: {self.name}, ID is: {self.id} and DoB is: {self.dob} ."