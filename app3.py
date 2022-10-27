class Animal:
    def __init__(self, name, ves, paroda):
        self.name = name
        self.ves = ves
        self.paroda = paroda

    def golos(self):
        pass

    def ShowInfo(self):
        print("Name: ", self.name, "Paroda: ", self.paroda, "Ves: ", self.ves)



class Dog(Animal):
    def __init__(self, name, ves, paroda):
        super().__init__(name, ves, paroda)


    def golos(self):
        print("Gav Gav")

class Cat(Animal):
    def __init__(self, name, ves, paroda):
        super().__init__(name, ves, paroda)

    def golos(self):
        print("Mau Mau")


mydog = Dog("bobik", 20, "Labrador")
mydog.ShowInfo()
mydog.golos()
myCat = Cat("Barsik", 5, "Bengal")
myCat.ShowInfo()
myCat.golos()

class CatDog(Cat, Dog):
    pass

catDog = CatDog("bill", 40, "catdog")
catDog.ShowInfo()




















