"""
    Menghitung konversi bilangan desimal 
    ke biner dan sebaliknya.
"""

print("==== KONVERSI BILANGAN DESIMAL DAN BINER ====")
print("1. Desimal ke Biner")
print("2. Biner ke Desimal")
print("=============================================")
pilihan = input("Pilih konversi (1/2): ")
if pilihan == '1':
    desimal = int(input("Masukkan bilangan desimal: "))
    biner = bin(desimal).replace("0b", "")
    print(f"Bilangan biner dari {desimal} adalah {biner}")
elif pilihan == '2':
    biner = input("Masukkan bilangan biner: ")
    desimal = int(biner, 2)
    print(f"Bilangan desimal dari {biner} adalah {desimal}")
else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")