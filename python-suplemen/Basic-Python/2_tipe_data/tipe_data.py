"""
    Sebelum kita memulai kode untuk string, ada yang perlu dijelaskan
    yaitu fungsi dalam print(). Fungsi print() digunakan untuk menampilkan
    ada berbagai macam cara penggunaan fungsi print() yaitu : 
    1. print("Hello World") -> menampilkan teks secara langsung
    2. print(variable) -> menampilkan isi dari sebuah variable
    3. print("teks", variable) -> menampilkan teks dan isi dari sebuah variable
    4. print("teks".format(variable)) -> menampilkan teks dengan variable yang di masukkan ke dalam teks tersebut
    5. print(f"teks {variable}") -> menampilkan teks dengan variable yang di masukkan ke dalam teks tersebut (cara ini lebih mudah di baca dan direkomendasikan) 

"""


#1. String
nama_saya = "Sharleen"
email_saya = "sharleen@ub.ac.id"
print(f"Nama saya adalah {nama_saya} dan tipe datanya adalah {type(nama_saya)}")
print(f"Email saya adalah {email_saya} dan tipe datanya adalah {type(email_saya)}")

#2. Integer
number = 25
id = 1
print(f"Angka saya adalah {number} dan tipe datanya adalah {type(number)}")
print(f"ID saya adalah {id} dan tipe datanya adalah {type(id)}")

#3. Float
kkm = 75.5
nilaiSaya = 100.0
print(f"KKM saya adalah {nilaiSaya} dan tipe datanya adalah {type(nilaiSaya)} saya melewati KKM yaitu {kkm} dan tipe datanya adalah {type(kkm)}")

#4. Boolean
benar = True
print(f"Benar itu adalah {benar} dan tipe datanya adalah {type(benar)}")

#5. Complex Number
angkaKompleks = 5 + 3j
print(f"Angka kompleks saya adalah {angkaKompleks} dan tipe datanya adalah {type(angkaKompleks)}")

#6. List
sahrleen = ["manajemen", 22, True]
nilai_saya = [90, 85, 88, 92]
kelulusan = [True, True, True, False]
print(f"Data saya adalah {sahrleen} dan tipe datanya adalah {type(sahrleen)}")
print(f"Nilai saya adalah {nilai_saya} dan tipe datanya adalah {type(nilai_saya)}")
print(f"Kelulusan saya adalah {kelulusan} dan tipe datanya adalah {type(kelulusan)}")

#7. Tuple
sharleen_tuple = ("sharleen", 22, "manajemen")
nilai_tuple = (90, 85, 88, 92)
kelulusan_tuple = (True, True, True, False)
print(f"Data saya adalah {sharleen_tuple} dan tipe datanya adalah {type(sharleen_tuple)}")
print(f"Nilai saya adalah {nilai_tuple} dan tipe datanya adalah {type(nilai_tuple)}")
print(f"Kelulusan saya adalah {kelulusan_tuple} dan tipe datanya adalah {type(kelulusan_tuple)}")

#8. Set
# Setting set
prodi = {'manajemen', 'teknik nuklir', 'komputer'}
nilai = {12, 13, 14}

# Modifikasi kode
prodi.add("siskom")
prodi.remove("teknik nuklir")
print(f"Prodi mahasiswa di universitas x adalah {prodi} dan tipe datanya adalah {type(prodi)}")
print(f"Nilai mahasiswa di universitas x adalah {nilai} dan tipe datanya adalah {type(nilai)}")

#9. Dictionary
hari = {
    "monday": "senin",
    "tuesday": "selasa",
    "wednesday": "rabu"
}
print(f"Hari dalam bahasa inggris dan indonesia adalah {hari} dan tipe datanya adalah {type(hari)}")

#10. Bytes
data_bytes = bytes(5)
print(f"Data bytes saya adalah {data_bytes} dan tipe datanya adalah {type(data_bytes)}")

#11. Bytearray
data_bytearray = bytearray(5)
print(f"Data bytearray saya adalah {data_bytearray} dan tipe datanya adalah {type(data_bytearray)}")

#12. Memoryview
angka_saya = memoryview(bytes(12))
angka_saya1 = memoryview(bytes(1212))
print(f"Data memoryview saya adalah {angka_saya} dan tipe datanya adalah {type(angka_saya)}")
print(f"Data memoryview saya adalah {angka_saya1} dan tipe datanya adalah {type(angka_saya1)}")

# Materi bonus (casting tipe data)
"""
    Casting Tipe Data di Python adalah 
    proses mengubah satu tipe data ke tipe data lainnya.
    sangat berfungsi pada syntaks input() yang secara default 
    menghasilkan tipe data string.
    Misalnya, jika kita ingin menerima input angka dari pengguna,   
    kita perlu mengubah tipe data string tersebut menjadi integer 
    atau float agar dapat melakukan operasi matematika.
"""
ini = "100"
print(f"Data awal: {ini} dengan tipe data: {type(ini)}")
# Mengubah string ke integer
ini_int = int(ini)
print(f"Data setelah di-casting: {ini_int} dengan tipe data: {type(ini_int)}")
# Mengubah string ke float
ini_float = float(ini)
print(f"Data setelah di-casting: {ini_float} dengan tipe data: {type(ini_float)}")
# Mengubah integer ke string
