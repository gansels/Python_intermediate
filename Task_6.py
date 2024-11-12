class Animals():
    total_weight = 0
    def __init__(self, weight):
        self.weight = weight
        Animals.total_weight += weight
    def set_weight(self, new_weight):
        Animals.total_weight -=self.weight
        self.weight = new_weight
        Animals.total_weight += new_weight

animals1 = Animals(5)
animals2 = Animals(3)

print("Total weight of both animals:" , Animals.total_weight)

# to change the animal weight one or two
animals2.set_weight(7)
print("Total weight of animals after change : ", Animals.total_weight)

