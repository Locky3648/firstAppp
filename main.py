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
        num = random.randint(1, 3)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()

        self.endOfDay()
        self.is_alive()

bodya = Student("bodya")
for day in range(365):
    if bodya.alive == False:
        break
    bodya.live(day)


































































