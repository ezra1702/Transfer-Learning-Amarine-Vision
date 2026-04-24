"""
    Operator Bitwise
        1. AND (&)          : Melakukan operasi AND pada setiap bit dari dua operand.
        2. OR (|)           : Melakukan operasi OR pada setiap bit dari dua operand.
        3. XOR (^)          : Melakukan operasi XOR pada setiap bit dari dua operand.
        4. NOT (~)          : Melakukan operasi NOT pada setiap bit dari operand.
        5. Left Shift (<<)  : Menggeser bit ke kiri sebanyak jumlah yang ditentukan.
        6. Right Shift (>>) : Menggeser bit ke kanan sebanyak jumlah yang ditentukan.
"""

operan_a = True # True sama dengan 1 dalam biner
operan_b = False # False sama dengan 0 dalam biner

# Operator AND (&)
hasil_and = operan_a & operan_b
print(f"Hasil AND {operan_a} & {operan_b} = {hasil_and}")

# Operator OR (|)
hasil_or = operan_a | operan_b
print(f"Hasil OR {operan_a} | {operan_b} = {hasil_or}")

# Operator XOR (^)
hasil_xor = operan_a ^ operan_b
print(f"Hasil XOR {operan_a} ^ {operan_b} = {hasil_xor}")

# Operator NOT (~)
hasil_not_a = ~operan_a
print(f"Hasil NOT ~{operan_a} = {hasil_not_a}")

# Operator Left Shift (<<)
a_copy = operan_a
print(f"Hasil Left Shift {operan_a} << 1 = {a_copy << 1}")

# Operator Right Shift (>>)
print(f"Hasil Right Shift {operan_a} >> 1 = {a_copy >> 1}")

# Operasi campuran
hasil_campuran = ((((operan_a & operan_b) | operan_a) ^ operan_b) << 1) & (~operan_a & ((operan_a | operan_b) >> 1) ^ ((((operan_a & operan_b) | operan_a) ^ operan_b) << 1))
print(f"Hasil Operasi Campuran = {hasil_campuran}")
