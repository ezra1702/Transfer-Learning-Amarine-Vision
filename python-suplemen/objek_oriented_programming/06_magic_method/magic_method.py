class Demo:
    # 2️Konstruktor
    def __init__(self, nilai):
        self.nilai = nilai

    # 1️Representasi
    def __str__(self):
        return f"Nilai user: {self.nilai}"

    def __repr__(self):
        return f"Demo(nilai={self.nilai})"

    # 3️Operasi aritmatika
    def __add__(self, other):
        return Demo(self.nilai + other.nilai)

    def __sub__(self, other):
        return Demo(self.nilai - other.nilai)

    def __mul__(self, other):
        return Demo(self.nilai * other.nilai)

    def __truediv__(self, other):
        return Demo(self.nilai / other.nilai)

    # 4️Perbandingan
    def __eq__(self, other):
        return self.nilai == other.nilai

    def __lt__(self, other):
        return self.nilai < other.nilai

    def __gt__(self, other):
        return self.nilai > other.nilai

    def __le__(self, other):
        return self.nilai <= other.nilai

    def __ge__(self, other):
        return self.nilai >= other.nilai

    # 5️Koleksi / container
    def __len__(self):
        return self.nilai

    def __getitem__(self, index):
        return self.nilai[index]

    def __setitem__(self, index, value):
        temp = list(self.nilai)
        temp[index] = value
        self.nilai = "".join(temp)

    def __contains__(self, item):
        return item in self.nilai

    # 6️Callable & context manager
    def __call__(self):
        print("Objek dipanggil seperti fungsi")

    def __enter__(self):
        print("Masuk blok with")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Keluar blok with")

    # 7️Atribut
    def __getattr__(self, name):
        return f"Atribut '{name}' tidak ada"

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f"Atribut {name} dihapus")
        object.__delattr__(self, name)

    # 2️Destruktor
    def __del__(self):
        print("Objek dihapus")

a = Demo(10)
b = Demo(5)

print(a)              # __str__
print(repr(a))        # __repr__

print(a + b)          # __add__
print(a > b)          # __gt__

obj = Demo("Python")
print(len(obj))       # __len__
print(obj[0])         # __getitem__
obj[0] = "J"          # __setitem__
print(obj)
print("J" in obj)     # __contains__

obj()                 # __call__

with Demo(100) as x:  # __enter__ & __exit__
    print(x)

print(obj.tidak_ada)  # __getattr__
