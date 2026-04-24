import random  
"""
    Materi yang akan di jelasakn disini yaitu : 
    1. List
    2. Tuple
    3. List Comprehension
    4. Dictionary
"""

# List : Bisa dimodifikasi setelah disetting
namaLengkap = ["Sharleen Alleta", "Geraldine Tiffany", "James Bond", "Donald Trump"]
prodi = ["Manajemen", "Data Science", "Teknik Mesin", "Teknik Komputer"]

# Tuple : Tidak bisa dimodifikasi setelah disetting
nim_default = ("225150307111009", "225150307111010", "225150307111011", "225150307111012")
nim = list(nim_default)
tanggalLahir_default = ("2002-01-01", "2002-01-02", "2002-01-03", "2002-01-04")
tanggalLahir = list(tanggalLahir_default)

# List comprehension
idMahasiswa = []
idMahasiswa = ([random.randint(1,10) if random.randint(1,10) not in idMahasiswa else random.randint(1,10) for _ in range(len(namaLengkap))])

# Directory : Membutuhkan key dan value
mahasiswa = {
    "namaLengkap" : namaLengkap,
    "namaDepan" : [nama.split()[0] for nama in namaLengkap],
    "namaBelakang" : [nama.split()[1] for nama in namaLengkap],
    "prodi" : prodi,
    "nim" : nim,
    "tanggalLahir" : tanggalLahir,
    "idMahasiswa" : idMahasiswa
}

def informasiMahasiswa():
    print("======= Informasi Mahasiswa =======")
    for i in range(len(mahasiswa["namaLengkap"])):
        print("====== Mahasiswa ke-" + str(i+1) + " ======")
        print(f"Nama Lengkap : {mahasiswa['namaLengkap'][i]}") 
        print(f"Nama Depan : {mahasiswa['namaDepan'][i]}")
        print(f"Nama Belakang : {mahasiswa['namaBelakang'][i]}")
        print(f"Prodi : {mahasiswa['prodi'][i]}")
        print(f"Nim : {mahasiswa['nim'][i]}")
        print(f"Tanggal Lahir : {mahasiswa['tanggalLahir'][i]}")
        print(f"ID Mahasiswa : {mahasiswa['idMahasiswa'][i]}")
        print("==================================")

# menambahkan data di akhir list 
def tambahMahasiswa(nama, prodi, nim, tanggalLahir):
    mahasiswa["namaLengkap"].append(nama) 
    mahasiswa["prodi"].append(prodi) 
    mahasiswa["nim"].append(nim)
    mahasiswa["tanggalLahir"].append(tanggalLahir)
    print("Mahasiswa berhasil ditambahkan.")

def cariMahasiswa(search):
  for i in range(len(mahasiswa["namaLengkap"])):
    if (search in mahasiswa("namaLengkap")[i].lower() or search in mahasiswa("namaDepan")[i].lower() or search in mahasiswa("namaBelakang")[i].lower() or search in mahasiswa("prodi")[i].lower() or search in mahasiswa("nim")[i].lower() or search in mahasiswa("tanggalLahir")[i].lower() or search in mahasiswa("idMahasiswa")[i].lower()):
      print("====== Mahasiswa ke-" + str(i+1) + " ======")
      print(f"Nama Lengkap : {mahasiswa['namaLengkap'][i]}")
      print(f"Nama Depan : {mahasiswa['namaDepan'][i]}")
      print(f"Nama Belakang : {mahasiswa['namaBelakang'][i]}")
      print(f"Prodi : {mahasiswa['prodi'][i]}")
      print(f"Nim : {mahasiswa['nim'][i]}")
      print(f"Tanggal Lahir : {mahasiswa['tanggalLahir'][i]}")
      print(f"ID Mahasiswa : {mahasiswa['idMahasiswa'][i]}")
      print("==================================")
    else :
      print("Mahasiswa tidak ditemukan.")

def hapusMahasiswa(search):
    for i in range(len(mahasiswa["namaLengkap"])):
        if (search in mahasiswa("namaLengkap")[i].lower() or search in mahasiswa("namaDepan")[i].lower() or search in mahasiswa("namaBelakang")[i].lower() or search in mahasiswa("prodi")[i].lower() or search in mahasiswa("nim")[i].lower() or search in mahasiswa("tanggalLahir")[i].lower() or search in mahasiswa("idMahasiswa")[i].lower()):
           del mahasiswa["namaLengkap"][i]
           del mahasiswa["namaDepan"][i]
           del mahasiswa["namaBelakang"][i]
           del mahasiswa["prodi"][i]
           del mahasiswa["nim"][i]
           del mahasiswa["tanggalLahir"][i]
           del mahasiswa["idMahasiswa"][i]
           print("Mahasiswa berhasil dihapus.")
           break

def ubahMahasiswa(search):
    for i in range(len(mahasiswa["namaLengkap"])):
        if (search in mahasiswa("namaLengkap")[i].lower() or search in mahasiswa("namaDepan")[i].lower() or search in mahasiswa("namaBelakang")[i].lower() or search in mahasiswa("prodi")[i].lower() or search in mahasiswa("nim")[i].lower() or search in mahasiswa("tanggalLahir")[i].lower() or search in mahasiswa("idMahasiswa")[i].lower()):
           change = input("======= Apa yang ingin Anda ubah :=======\n 1.Nama Lengkap \n 2.prodi \n 3.Nim \n 4.Tanggal Lahir \n =======================\n Pilihan Anda : (1/2/3/4) ")
           if change == "1":
               nama = input("Masukkan nama lengkap: ")
               mahasiswa["namaLengkap"][i] = nama
           elif change == "2":
               prodi = input("Masukkan prodi: ")
               mahasiswa["prodi"][i] = prodi
           elif change == "3":
               nim = input("Masukkan nim: ")
               mahasiswa["nim"][i] = nim
           elif change == "4":
               tanggalLahir = input("Masukkan tanggal lahir: ")
               mahasiswa["tanggalLahir"][i] = tanggalLahir
           else:
               print("Pilihan tidak valid. Silakan pilih 1, 2, 3 atau 4.")
           print("Mahasiswa berhasil diubah.")

while True : 
    print("======= Menu Pilihan =======")
    print("1. Menampilkan Semua Informasi Mahasiswa")
    print("2. Menambah Mahasiswa")
    print("3. Mencari Mahasiswa")
    print("4. Menghapus Mahasiswa")
    print("5. Mengubah Mahasiswa")
    print("============================")
    pilihan = int(input("Masukkan pilihan (1-5): "))

    if pilihan == 1:
        informasiMahasiswa()
    elif pilihan == 2:
        flag = 1
        while flag == 1:
            nama = input("Masukkan nama lengkap: ")
            prodi = input("Masukkan prodi: ")
            nim = input("Masukkan nim: ")
            tanggalLahir = input("Masukkan tanggal lahir: ")
            tambahMahasiswa(nama, prodi, nim, tanggalLahir)
            ulang = input("Apakah Anda ingin menambahkan mahasiswa lagi? (y/n): ")
            # write one line if statement
            if ulang.lower() != 'y':flag = 0
    elif pilihan == 3:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        cariMahasiswa(search)
    elif pilihan == 4:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        hapusMahasiswa(search)
    elif pilihan == 5:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        ubahMahasiswa(search)
    else:
        print("Pilihan tidak valid.")

    ulang = input("Apakah Anda ingin menggunakan program ini lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih telah menggunakan program ini.")
        break




