"""
    Operator Aritmatika
        1. Penjumlahan (+)     : Menjumlahkan dua operand.
        2. Pengurangan (-)     : Mengurangi operand kedua dari operand pertama.
        3. Perkalian   (*)     : Mengalikan dua operand.
        4. Pembagian   (/)     : Membagi operand pertama dengan operand kedua.
        5. Modulus     (%)     : Menghasilkan sisa pembagian dari dua operand.
        6. Eksponen    (**)    : Menghasilkan pangkat dari operand pertama berdasarkan operand kedua.
        7. Floor Division (//) : Membagi operand pertama dengan operand kedua dan menghasilkan hasil pembagian tanpa desimal.
"""

operand_a = 10
operand_b = 20


# Operator Penjumlahan(+) 
hasil_penjumlahan = operand_a + operand_b
print(f"Hasil Penjumlahan {operand_a} + {operand_b} = {hasil_penjumlahan}")

# Operator Pengurangan(-)
hasil_pengurangan = operand_a - operand_b
print(f"Hasil Pengurangan {operand_a} - {operand_b} = {hasil_pengurangan}")

# Operator Perkalian(*)
hasil_perkalian = operand_a * operand_b
print(f"Hasil Perkalian {operand_a} * {operand_b} = {hasil_perkalian}")

# Operator Pembagian(/)
hasil_pembagian = operand_a / operand_b
print(f"Hasil Pembagian {operand_a} / {operand_b} = {hasil_pembagian}")

# Operator Modulus(%)
hasil_modulus = operand_a % operand_b
print(f"Hasil Modulus {operand_a} % {operand_b} = {hasil_modulus}")

# Operator Eksponen(**)
hasil_eksponen = operand_a ** operand_b
print(f"Hasil Eksponen {operand_a} ** {operand_b} = {hasil_eksponen}")

# Operator Floor Division(//)
hasil_floor_division = operand_a // operand_b
print(f"Hasil Floor Division {operand_a} // {operand_b} = {hasil_floor_division}")