"""
    Luas Segita Perhitungan
"""

print("== Rumus Luas Segitiga ==")
panjang = float(input("Masukkan panjang alas segitiga (dalam satuan cm): "))
tinggi = float(input("Masukkan tinggi segitiga (dalam satuan cm): "))
luas_segitiga = 0.5 * panjang * tinggi
for i in range(3):
    print(f"{i+1}")

print(f"Luas segitiga dengan alas {panjang} cm dan tinggi {tinggi} cm adalah {luas_segitiga} cm²")