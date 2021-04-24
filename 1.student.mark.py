class Student:
#n = int(input("Number of students in a class : "))
#m = int(input("Number of courses : "))
def getStudent(self):
    self.name = input("Enter Name : ")
    self.id = input("Enter ID : ")
    self.dob = input("Enter Date of Birth : ")

    self.cid = input("Enter Course ID : ")
    self.cname = input("Enter Course Name : ")
    self.mark = int(input("Enter mark in this course : "))
def Print(self):
    print(self.name, self.id, self.dob, self.cid, self.cname, self.mark)
S1 = Student()
S1.getStudent()
print(" Student : ")
S1.printPrint()