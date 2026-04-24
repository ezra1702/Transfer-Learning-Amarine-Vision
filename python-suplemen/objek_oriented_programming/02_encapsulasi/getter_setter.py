import random
class Amarine:
    _unit_total = 0
    _price_total = 0
    def __init__(self, id, name, type, price =0):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__price = price
    
    @property
    def info(self):
        return f"=========================\nNama Kapal: {self.__name}\nTipe Kapal: {self.__type}\nHarga Kapal: Rp. {self.__price:,}"
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    


amarine1 = Amarine(random.randint(1,100), "AMN-01", "Fishing Boat")

print(amarine1.info)
amarine1.price = 100000000
print(amarine1.info)


