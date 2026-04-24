"""
    Perulangan menenetukan nilai max, min, rata, rata serta megurutkan nilai dari sekumpulan data.
"""
while True:
    print("==== MENGHITUNG NILAI MAX, MIN, RATA-RATA DARI SEKUMPULAN DATA ====")
    print("1. Hitung Nilai Max")
    print("2. Hitung Nilai Min")
    print("3. Hitung Nilai Rata-Rata")
    print("4. Urutkan Nilai")
    print("===============================================================")
    pilihan = input("Pilih operasi (1/2/3/4): ")
    jumlah_data = int(input("Masukkan jumlah data: "))
    banyak = []
    for i in range(0, jumlah_data): # dimulai dari 0 sampai jumlah_data-1
        data = int(input(f"Masukkan data ke-{i+1}: "))
        banyak.append(data)
    print("Data yang dimasukkan:", banyak)
    if pilihan == '1':
        print(f"Nilai Max dari data tersebut adalah {max(banyak)}")
    elif pilihan == '2':
        print(f"Nilai Min dari data tersebut adalah {min(banyak)}")
    elif pilihan == '3':
        print(f"Nilai Rata-Rata dari data tersebut adalah {sum(banyak)/len(banyak)}")
    elif pilihan == '4':
        print(f"Data yang diurutkan adalah {sorted(banyak)}")
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3 atau 4.")
    ulang = input("Apakah Anda ingin mengulang? (y/n): ")
    if ulang.lower() != 'y':
        print("Terima kasih telah menggunakan program ini.")
        break
    print("\n")  