class TimeMeasurement:
    pass
with TimeMeasurement() as t:
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo)
import time


class TimeMeasurment:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.start_time = None
        self.end_time = None

    def __enter__(self):
        self.start_time = time.time()
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.end_time = time.time()
        duration_time = self.end_time - self.start_time
        self.file.close()

        print(f"Start to calculate the start time: (time.time(self.start_time)")
        print(f"Start to calculate the End time: (time.time(self.end_time)")
        print(f"lasted time{duration_time:.2f}second")


with TimeMeasurment("test.txt", 'w') as t:  # "Spouštím výpočet v čase 18:59.03"
    cislo = 1
    for i in range(10000000):
        cislo += i
    print(cislo)  # 49999995000001
# "Dokončeno v čase 18:59.05 - blok trval 3 sekundy

