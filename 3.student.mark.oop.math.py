import math
import curses
import time

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

class Cource:
    def __init__(self, ci, cn):
        self.cname = cn
        self.cid = ci

    def get_cn(self):
        return self.cname

    def get_ci(self):
        return self.cid

    def cource_des(self):
        print("Cource Name",self.cname)
        print("Cource Id: ",self.cid)
    
    def __str__(self):
        return f"Cource name is:{self.cname}, Cource Id is: {self.cid} ."


class StudentMark(Number):
    def __init__(self, s, c, m, credit):
        self.student = s
        self.cource = c
        self._mark = m
        self.credit = credit
    
    def get_s(self):
        return self.student

    def get_c(self):
        return self.cource

    def get_m(self):
        return self.mark

    def get_credit(self):
        return self.credit

    def mark_des(self):
        print("Student:",self.student)
        print("Cource: ",self.cource)
        print("Mark:",self._mark)

    def mark_round(self):
        self.mark= round(self._mark,1)

    def __str__(self):
        return f"Student name is: {self.student}, Cource is:{self.cource}, Mark is:{self.mark} ."
    
    #def round(number,1):
    #    math.floor(number*10)/10

    def GPA(self):
        total_mark = 0

        total_mark += self.mark
        total_credit = self.numbcource
        self.gpa = total_mark/ total_credit

    def printGPA(self):
        print("Grade point everage(GPA):", self.gpa)

    #sort stu by GPA(gpa max 10)
    def sort(self):
        if self.gpa in range(8,10):
            print("Exellent!")
        elif self.gpa in range(5,7):
            print("Good, enought to pass!")
        elif self.gpa in range(1,4):
            print("Not pass!")
    
#curses : 
menu = ['Student','Cource','Mark','Exit']
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
    x = w//2 - len(row)//2
    y = h//2 - len(menu)//2 + idx
    if idx == selected_row_idx:
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(y, x, row)
        stdscr.attroff(curses.color_pair(1))
    else:
        stdscr.addstr(y, x, row)
    stdscr.refresh()
    time.sleep(3)

def main(stdscr):
    curses.set_curs(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curent_row_idx = 0
    print_menu(stdscr, curent_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()
        if key ==curses.Key_up and curent_row_idx > 0:
            curent_row_idx -= 1
        elif key ==curses.Key_down and curent_row_idx < len(menu)-1:
            curent_row_idx += 1
        elif key == curses.Key_enter or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, "You pressed {}".format(menu[curent_row_idx]))
            stdscr.refresh()
            if curent_row_idx == len(menu)-1:
                break

        print_menu(stdscr, curent_row_idx)
        stdscr.refresh()


curses.wrapper(print_menu)