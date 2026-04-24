# section 1


def hello():
    print("Hello Bellshade !")


hello()  # Hello!

# section 2 => parameter


def selamat(nama):
    print(f"Hello {str(nama)} !")


selamat("World")  # Hello World !

# section 3 => perhitungan


def triangle(alas, tinggi):
    hasil = (alas * tinggi) / 2
    print(hasil)


triangle(2, 3)

# section 4 => return
"""
   Konsep return pada fungsi adalah mengembalikan nilai dari sebuah fungsi
   maksusudnya, ketika sebuah fungsi dipanggil, fungsi tersebut dapat mengembalikan
    sebuah nilai yang dapat disimpan dalam variabel atau digunakan langsung.
"""


def segitiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    return hasil


luas = segitiga(4, 5)
print(luas)  # 10.0

# section 5 => default parameter


def salam(waktu="Pagi"):
    greet = "Selamat " + str(waktu)
    return greet


print(salam("Siang"))  # Selamat Siang
print(salam("Malam"))  # Selamat Malam
print(salam("Sore"))  # Selamat Sore
print(salam())  # Selamat Pagi

# section 6 => unlimited parameter : *args berfungsi untuk menerima sejumlah argumen yang tidak terbatas


def unlimited(*args):
    for item in args:
        print(item)


unlimited(1, 2, 3, 4)
unlimited([1, 2], [3, 4])

# section 7 +> unlimited keyword : **kwargs berfungsi untuk menerima sejumlah argumen kata kunci yang tidak terbatas


def unlimitedkeyword(**infinite):
    for key, value in infinite.items():
        print(f"index {key} memiliki nilai {value}")


unlimitedkeyword(a=2, b=1, c=3)
unlimitedkeyword(fname="Harry", lname="Potter")

""" 
    Perbedaan antara *args dan **kwargs adalah:
    1. *args digunakan untuk mengirim sejumlah argumen non-kata kunci (psositional arguments) ke dalam fungsi,
        contohnya jika kita ingin mengirim beberapa nilai numerik ke dalam fungsi. kita dapat menggunakan *args untuk mengumpulkan
        nilai-nilai tersebut menjadi sebuah tuple di dalam fungsi. sehingga kita dapat mengakses setiap nilai tersebut secara individual di dalam fungsi.
    2. **kwargs digunakan untuk mengirim sejumlah argumen kata kunci (keyword arguments) ke dalam fungsi,
        contohnya jika kita ingin mengirim beberapa pasangan kunci-nilai ke dalam fungsi. kita dapat menggunakan **kwargs untuk mengumpulkan
        pasangan kunci-nilai tersebut menjadi sebuah dictionary di dalam fungsi. sehingga kita dapat mengakses setiap pasangan kunci-nilai tersebut secara individual di dalam fungsi.
"""