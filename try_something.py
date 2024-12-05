# Task4
class Car:
    def __init__(self,brand, color):
        self.brand = brand
        self.color = color
        self.mileage = 0
    def go_shopping(self):
        self.mileage += 10
car1 = Car("Ferrari", "Red")
print(car1.brand)

class Animals:
    def __init__(self,weight, age, look, breath):
        self.weight = weight
        self.age = age
        self.look = look
        self.breath = breath
    def __str__(self):
        return f"weight: {self.weight}, Age: is {self.age}, Look: {self.look}, Breath: {self.breath}"
class Fish(Animals):
    def __init__(self,weight, age, look, breath,swim):
        super().__init__(weight, age, look, breath)
        self.swim = swim
    def __str__(self):
        return f"{super().__str__()}, Swim: {self.swim}"
class Mammals(Animals):
    def __init__(self,weight, age, look, breath, run):
        super().__init__(weight, age,look,breath)
        self.run = run
    def __str__(self):
        return f"{super().__str__()}, Run: {self.run}"
class Bird(Animals):
    def __init__(self,weight, age, look, breath, fly):
        super().__init__(weight, age, look, breath)
        self.fly = fly
    def __str__(self):
        return f"{super().__str__()}, Fly: {self.fly}"

class Domestic_dog(Animals):
    def__init__(self,weight, age, look, breath, run, breed, coat_color, bark, retrive):
        super().__init__(weight, age,look, breath,run)
        self.breed = breed
        self.coat_color = coat_color
        self.bark = bark
        self.retrieve = retrieve
    def __str__(self):
        return f"{super().__str__()}, Breed: {self.breed}, Coat color: {self.coat_color}, Bark: {self.bark}, Retrieve: {self.retrieve}"


fish = Fish(weight=3, age=3,look="Wild", Breath="Trout", swim=True)
print(fish)
mammal = Mammals(weight=60, age=5, look="Furry", breath="Lungs", run=True)
print(mammal)

bird = Bird(weight=1, age=2, look="Feathers", breath="XYZ", fly=True)
print(bird)

dog = Domestic_dog(weight=25, age=3, look="Furry", breath="Lungs", run=True, breed="Labrador", coat_color="Yellow", bark=True, retrieve=True)
print(dog)

#Task 5:
# DomesticActivities(Fish, Mammals):
 #   pass
#animals = Animals(3,10)
#print(animals)



