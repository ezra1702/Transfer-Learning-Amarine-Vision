""" 
    Operator Logika dalam Python
    => Digunakan untuk menggabungkan pernyataan logika.
    1. and    : Mengembalikan True jika kedua operand bernilai True.
    2. or     : Mengembalikan True jika salah satu operand bernilai True

"""
nilai = 70

print("Index nilai adalah A" if nilai > 80 else "Index nilai adalah B" if nilai >= 75 and nilai <= 80 else "Index nilai adalah C")