class Amarine:
    # class variable => dimiliki oleh class dan dibagikan ke semua objek (instance)
    price_total = 0
    unit_total = 0
    #Constructor
    def __init__(self, name, type):
        # instace variable => dimiliki oleh objek tetapi tidak dimiliki oleh class
        self.name = name
        self.type = type
        self.price = 0
    # Methods
    # method dengan argumen
    def addPrice(self, price):
       self.price += price

    def totalPrice(self,price):
        Amarine.price_total += price
        print(f"Total Harga Kapal: Rp. {Amarine.price_total:,}")

    def totalUnit(self):
        Amarine.unit_total += 1
        print(f"Total Kapal: {Amarine.unit_total}")
    # Method dengan return
    def getType(self):
        return self.type

    # void function (method tanpa argumen)
    def info(self):
        print(f"Nama Kapal: {self.name}")
        print(f"Tipe Kapal: {self.type}")
        self.totalPrice(self.price)
        print(f"Harga Kapal: Rp. {self.price:,}")
        self.totalUnit()
        print("=================================")

amarine1 = Amarine("AMN-01", "Fishing Boat")
amarine2 = Amarine("AMN-02", "Armed Boat")
amarine3 = Amarine("AMN-03", "Attack Boat")
amarine4 = Amarine("AMN-04","Defense Boat")

amarine_armada = [amarine1, amarine2, amarine3, amarine4]
amarine1.addPrice(100000000)
amarine2.addPrice(200000000)
amarine3.addPrice(300000000)
amarine4.addPrice(400000000)
print("====== Informasi Kapal ======")
for i in  amarine_armada:
    i.info()



    



