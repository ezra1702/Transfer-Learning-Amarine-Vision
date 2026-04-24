import random
from colorama import Fore, Back, Style

class Amarine:
    _unit_total = 0
    _price_total = 0
    def __init__(self, id, name, type, price =0):
        self._id = id
        self._name = name
        self._type = type
        self._price = price
    
    @property
    def info(self):
        return Fore.GREEN  + f"=========================\nNama Kapal: {self.__name}\nTipe Kapal: {self.__type}\nHarga Kapal: Rp. {self.__price:,}"
    


class AUV(Amarine):
    # def __init__(self, id, name, type):
    #     self.__id = id
    #     self.__name = name
    #     self.__type = type
    #     self.__price = 10000000
    # # Output Error
    def __init__(self, id, name, type):
        # Amarine.__init__(self, id, name, type, price=10000000)
        super().__init__(id, name, type, price=10000000)
        
    #Override atribut info dari Amarine
    @property
    def info(self):
            return Fore.RED + f"Ini tipe AUV\n=========================\nNama Kapal: {self._name}\nTipe Kapal: {self._type}\nHarga Kapal: Rp. {self._price:,}" 
    


amarine1 = AUV(random.randint(1,100), "AMN-01", "Fishing Boat")
print(amarine1.info)
print(amarine1.__dict__)




