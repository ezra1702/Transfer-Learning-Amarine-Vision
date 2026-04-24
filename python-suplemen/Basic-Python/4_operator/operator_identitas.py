"""
    Operator Identitas 
        => Digunakan untuk membandingkan objek, bukan nilai dari objek tersebut.
        1. is        : Memeriksa apakah dua variabel merujuk ke objek yang sama di memori.
        2. is not    : Memeriksa apakah dua variabel tidak merujuk ke objek yang sama di memori.
"""

a = [1, 2, 3]
b = 3

if b is a[2]:
    print(f"{b} is {a[2]}: True")
else:
    print(f"{b} is {a[2]}: False")

if b is not a[1]:
    print(f"{b} is not {a[1]}: True")
else:
    print(f"{b} is not {a[1]}: False")