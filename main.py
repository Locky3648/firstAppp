# print("Hello from itstep")
#
# class Student:
#     count_students = 0
#     def __init__(self, name, height):
#         self.name =  name
#         self.height  =  height
#         Student.count_students += 1
#
#     def printer(self):
#         print("Name: ", self.name, " Height:", self.height)
#
#
#     def set_name(self, newName):
#         self.name = newName
#
#
#
#
# first_student = Student("Zielensky", 180)
# first_student.printer()
#
# first_student.set_name("Aristovich")
# first_student.printer()
#
# second_student = Student("Putler", 150)
# second_student.printer()
# #print(Student.count_students)

import  random


class Student:
    def __init__(self, name):
        self.name = name
        self.money = 50
        self.gladness = 50
        self.progress = 0
        self.alive = True


    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3


    def to_chill(self):
        print("Rest Time!")
        self.progress -= 0.12
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("You Lox")
            self.alive = False
        elif self.gladness <= 0:
            print("Ne uspel otdoxnut ty v dipresii")
            self.alive = False

    def endOfDay(self):
        print("Gladness:  ", self.gladness)
        print("Progress:   ", self.progress)

    def live(self,day):
        print("Day",str(day), " of ", self.name, "life")
        num = random.randint(1, 4)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()
        elif num == 4:
            self.money()



        self.endOfDay()
        self.is_alive()


    def money(self):
        print("Time to work")
        self.progress -= 1
        self.gladness -= 1
        self.money += 50



class Gruppa:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.countStudent = 0

    def addStudents(self, student):
        self.students.append(student)     # добавляем нового пассажира в массив
        self.countStudent += 1

    def printStudentsNames(self):
        if self.students != []:
            print("Name of the gruppa: ", self.name, "\nCount students: ", self.countStudent)
            for ps in self.students:
                print("Name of students: ", ps.name)

        else:
            print("No students in gruppa!")

    def delStudent(self, delStudent):
        try:
            self.students.remove(delStudent)
        except:
            print("There are no such student")

    def simulateGrupp(self):
        for st in self.students:
            for day in range(365):
                if st.alive == False:
                    self.delStudent(st)
                    break
                st.live(day)










nick = Student("Nick")
Bobik = Student("Bobik")

gruppa1 = Gruppa("Itstep")

gruppa1.delStudent(nick)
gruppa1.addStudents(Bobik)


gruppa1.printStudentsNames()










bodya = Student("bodya")
for day in range(365):
    if bodya.alive == False:
        break
    bodya.live(day)


































































