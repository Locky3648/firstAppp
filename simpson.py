class Human:
    def __init__(self, name):
        self.name = name



class Car:
    def __init__(self, brand):
        self.brand = brand
        self.countPassenger = 0
        self.passengers = [] # массив объектов Human


    def addPassanger(self, human):
        self.passengers.append(human)     # добавляем нового пассажира в массив
        self.countPassenger += 1

    def printPassengerNames(self):
        if self.passengers != []:
            print("Name of the car: ", self.brand, "\nCount passenger: ", self.countPassenger)
            for ps in self.passengers:
                print("Name of passanger: ", ps.name)

        else:
            print("No passangers in the car!")

nick = Human("Nick")
Bobik = Human("Bobik")

car1 = Car("Mers")

car1.addPassanger(nick)
car1.addPassanger(Bobik)

car1.printPassengerNames()

































































































































































































