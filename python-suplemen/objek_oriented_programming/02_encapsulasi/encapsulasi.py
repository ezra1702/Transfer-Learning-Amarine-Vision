import random
class Amarine:
    _unit_total = 0
    _price_total = 0
    def __init__(self,id, name, type, price =0):
        self.__id = id
        self.__name = name
        self.__type = type
        self.price = price
        Amarine._unit_total += 1
    #getter
    def getName(self):
        return self.__name
    def getType(self):
        return self.__type
    
    #setter
    def setName(self, name):
        self.__name = name

    def setType(self, type):
        self.__type = type

    def addPrice(self, price_components):
        self.price += price_components
        self._price_total += price_components
    def totalPrice(self):
        print(f"Total Harga Kapal: Rp. {self._price_total:,}")
    def totalUnit(self):
        print(f"Total Kapal: {Amarine._unit_total}")
    def info(self):
        print(f"Nama Kapal: {self.getName()}")
        print(f"Tipe Kapal: {self.getType()}")
        self.totalPrice()
        print(f"Harga Kapal: Rp. {self.price:,}")
        self.totalUnit()
        print("=================================")

nilai_random = random.randint(1,100)

amarine1 = Amarine(nilai_random, "AMN-01", "Fishing Boat")
amarine2 = Amarine(nilai_random, "AMN-02", "Armed Boat")
amarine3 = Amarine(nilai_random, "AMN-03", "Attack Boat")
amarine4 = Amarine(nilai_random, "AMN-04","Defense Boat")
container = [amarine1, amarine2, amarine3, amarine4]

for i in container:
    i.addPrice(random.randint(10000000, 99999999))

for i in container:
    i.info()

