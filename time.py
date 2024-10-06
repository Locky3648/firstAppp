import datetime

class Student:
    def __init__(self, name, birth_year, group, average_grade):
        self.name = name
        self.birth_year = birth_year
        self.group = group
        self.average_grade = average_grade

    def __str__(self):
        return (f"Ім'я: {self.name}\n"
                f"Рік народження: {self.birth_year}\n"
                f"Група: {self.group}\n"
                f"Середній бал: {self.average_grade:.2f}")

    def get_age(self):
        current_year = datetime.date.today().year
        return current_year - self.birth_year

# Приклад використання
student = Student("Ілля", 2009, "1111", 8.5)
print(student)
print(f"Вік студента: {student.get_age()} років")
