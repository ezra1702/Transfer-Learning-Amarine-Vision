"""
    Operator Penugasan 
        => Digunakan untuk menetapkan nilai ke variabel.
        1. =       : Menetapkan nilai dari kanan ke kiri.
        2. +=      : Menambahkan nilai di sebelah kanan ke variabel di sebelah kiri dan menetapkan hasilnya ke variabel di sebelah kiri.
        3. -=      : Mengurangi nilai di sebelah kanan dari variabel di sebelah kiri dan menetapkan hasilnya ke variabel di sebelah kiri.
        4. *=      : Mengalikan nilai di sebelah kanan dengan variabel di sebelah kiri dan menetapkan hasilnya ke variabel di sebelah kiri.
        5. /=      : Membagi variabel di sebelah kiri dengan nilai di sebelah kanan dan menetapkan hasilnya ke variabel di sebelah kiri.
        6. %=      : Menghitung sisa pembagian variabel di sebelah kiri dengan nilai di sebelah kanan dan menetapkan hasilnya ke variabel di sebelah kiri.
        7. //=     : Melakukan pembagian lantai pada variabel di sebelah kiri dengan nilai di sebelah kanan dan menetapkan hasilnya ke variabel di sebelah kiri.
        8. **=     : Menaikkan variabel di sebelah kiri ke pangkat nilai di sebelah kanan dan menetapkan hasilnya ke variabel di sebelah kiri.
"""

# =
a = 10
print(f"Nilai a setelah penugasan (=) adalah {a}")

# +=
a += 5
print(f"Nilai a setelah penugasan (+=) adalah {a}")

# -=
a -= 3
print(f"Nilai a setelah penugasan (-=) adalah {a}") 

# *=
a *= 2
print(f"Nilai a setelah penugasan (*=) adalah {a}")

# /=
a /= 4
print(f"Nilai a setelah penugasan (/=) adalah {a}")

# %=
a %= 3
print(f"Nilai a setelah penugasan (%=) adalah {a}")

# //=
a //= 1
print(f"Nilai a setelah penugasan (//=) adalah {a}")

# **=
a **= 3
print(f"Nilai a setelah penugasan (**=) adalah {a}")

# Kombinasi beberapa operator penugasan