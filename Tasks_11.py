class Iterator:
    def __init__(self, num):
        self.num = num
        self.numbers = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.numbers > self.num:
            raise StopIteration
        result = self.numbers ** 2
        self.numbers += 1
        return result

powers = Iterator(5)
for power in powers:
    print(power)