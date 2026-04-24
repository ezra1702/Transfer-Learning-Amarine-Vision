from abc import ABC, abstractmethod

class Amarine(ABC):

    @abstractmethod
    def menyelam(self):
        pass

    @abstractmethod
    def bergerak(self):
        pass

    @abstractmethod
    def status(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan metode status")

class AUV(Amarine):

    def menyelam(self):
        return "AUV menyelam otomatis"

    def bergerak(self):
        return "AUV navigasi mandiri"

    def status(self):
        return "AUV: Mode autonomous"

    def misi_otomatis(self):
        return "Menjalankan misi survey laut"

class ROV(Amarine):

    def menyelam(self):
        return "ROV menyelam dengan kontrol operator"

    def bergerak(self):
        return "ROV dikendalikan dari kapal"


    def lengan_robot(self):
        return "Mengambil sampel laut"
    
class OUV(Amarine):

    def menyelam(self):
        return "OUV menyelam dengan kontrol operator"

    def bergerak(self):
        return "OUV dikendalikan dari kapal"
    
    def status(self):
        super().status()


auv = AUV()
# rov = ROV() # error dikarenakan abastract dari Amarine ada yang belum di implementasikan
ouv = OUV()

print(auv.menyelam())
print(ouv.status())
