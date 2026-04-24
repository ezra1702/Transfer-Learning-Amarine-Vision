import mahasiswa

while True:
    print("======= Menu Pilihan =======")
    print("1. Menampilkan Semua Informasi Mahasiswa")
    print("2. Menambah Mahasiswa")
    print("3. Mencari Mahasiswa")
    print("4. Menghapus Mahasiswa")
    print("5. Mengubah Mahasiswa")
    print("============================")
    pilihan = int(input("Masukkan pilihan (1-5): "))
    if pilihan == 1:
        mahasiswa.informasiMahasiswa()
    elif pilihan == 2:
        flag = 1
        while flag == 1:
            nama = input("Masukkan nama lengkap: ")
            prodi = input("Masukkan prodi: ")
            nim = input("Masukkan nim: ")
            tanggalLahir = input("Masukkan tanggal lahir: ")
            mahasiswa.tambahMahasiswa(nama, prodi, nim, tanggalLahir)
            ulang = input("Apakah Anda ingin menambahkan mahasiswa lagi? (y/n): ")
            # write one line if statement
            if ulang.lower() != 'y':flag = 0
    elif pilihan == 3:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        mahasiswa.cariMahasiswa(search)
    elif pilihan == 4:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        mahasiswa.hapusMahasiswa(search)
    elif pilihan == 5:
        search = input("Masukan Informasi apapun tentang mahasiswa: ")
        mahasiswa.ubahMahasiswa(search)
    else:
        print("Pilihan tidak valid.")
    ulang = input("Apakah Anda ingin menggunakan program ini lagi? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih telah menggunakan program ini.")
        break