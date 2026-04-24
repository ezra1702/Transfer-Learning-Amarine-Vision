# String Python
<center>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPHD9iTWwYDqCIDxU-GiuckH6_kqyyPJc9Pg&s">
</center>
## Daftar Isi

- [Pendahuluan](#pendahuluan)
- [Deklarasi Variabel String](#deklarasi-variabel-string)
- [Deklarasi Variabel Multistring](#deklarasi-variabel-multistring)
- [Mencetak String](#mencetak-string)
- [Method String Bawaan](#method-string-bawaan)
  - [upper()](#upper)
  - [lower()](#lower)
  - [title()](#title)
  - [capitalize()](#capitalize)
  - [replace()](#replace)
  - [split()](#split)
  - [join()](#join)
  - [find()](#find)
  - [count()](#count)
  - [startswith()](#startswith)
  - [endswith()](#endswith)
  - [len()](#len)
  - [Substring dan Slicing](#substring-dan-slicing)
  - [Operator in](#operator-in)
- [Video Penjelasan](#video-penjelasan)
- [Hands-On](#hands-on)
- [Materi Selanjutnya](#materi-selanjutnya)

## Pendahuluan

String adalah salah satu tipe data pada Python yang digunakan untuk menyimpan teks atau karakter. String sangat penting ketika kita ingin menyimpan data seperti nama, alamat, deskripsi, dan informasi teks lainnya. Dalam Python, string ditulis dengan tanda kutip tunggal (`'`) atau ganda (`"`).

## Deklarasi Variabel String

```python
kata_pertama = "warung"
nama = "Sharleen Aletta"

# String juga dapat ditulis menggunakan petik satu
# Contoh: kata_pertama = 'warung'
# Namun konsistensi dalam penggunaan tanda kutip sangat disarankan
```

## Deklarasi Variabel Multistring

Python mendukung string multiline menggunakan tiga tanda kutip (baik tunggal atau ganda):

```python
kata_saya = """Indonesia adalah negara yang indah
berada di bawah garis khatulistiwa
aku cinta Indonesia
"""

# Atau dengan tiga tanda kutip tunggal
lagu = '''Lihat kebunku
penuh dengan bunga
ada yang putih dan ada yang merah
'''
```

## Mencetak String

```python
print(kata_saya)

# Output:
# Indonesia adalah negara yang indah
# berada di bawah garis khatulistiwa
# aku cinta Indonesia
```

## Method String Bawaan

Python menyediakan banyak method bawaan untuk memanipulasi string. Berikut adalah beberapa yang paling umum digunakan:

### upper()

Method ini mengubah semua karakter dalam string menjadi huruf kapital.

```python
name = "Sharleen Aletta"
print(name.upper())  # Output: SHARLEEN ALETTA
```

### lower()

Method ini mengubah semua karakter dalam string menjadi huruf kecil.

```python
name = "Sharleen Aletta"
print(name.lower())  # Output: sharleen aletta
```

### title()

Method ini mengubah setiap kata dalam string menjadi format judul (huruf pertama kapital, lainnya kecil).

```python
name = "Sharleen Aletta"
print(name.title())  # Output: Sharleen Aletta
```

### capitalize()

Method ini mengubah huruf pertama string menjadi kapital dan sisanya menjadi huruf kecil.

```python
name = "Sharleen Aletta"
print(name.capitalize())  # Output: Sharleen aletta
```

### replace()

Method ini mengganti substring tertentu dengan substring lain.

```python
name = "Sharleen Aletta"
print(name.replace("Aletta", "Smith"))  # Output: Sharleen Smith
```

### split()

Method ini membagi string menjadi list berdasarkan separator (default: spasi).

```python
name = "Sharleen Aletta"
print(name.split())  # Output: ['Sharleen', 'Aletta']

# Dengan separator tertentu
tanggal = "2024-01-15"
print(tanggal.split("-"))  # Output: ['2024', '01', '15']
```

### join()

Method ini menggabungkan elemen-elemen iterable (seperti list) menjadi sebuah string dengan separator tertentu.

```python
name = "Sharleen Aletta"
bagian = name.split()  # ['Sharleen', 'Aletta']
print("-".join(bagian))  # Output: Sharleen-Aletta
```

### find()

Method ini mencari substring dalam string dan mengembalikan indeks pertama kemunculannya. Mengembalikan -1 jika tidak ditemukan.

```python
name = "Sharleen Aletta"
print(name.find("Sharleen"))  # Output: 0
print(name.find("e"))         # Output: 5 (indeks pertama huruf 'e')
print(name.find("z"))         # Output: -1 (tidak ditemukan)
```

### count()

Method ini menghitung berapa kali substring muncul dalam string.

```python
name = "Sharleen Aletta"
print(name.count("e"))    # Output: 3
print(name.count("a"))    # Output: 2
```

### startswith()

Method ini memeriksa apakah string dimulai dengan substring tertentu.

```python
name = "Sharleen Aletta"
print(name.startswith("Shar"))  # Output: True
print(name.startswith("John"))  # Output: False
```

### endswith()

Method ini memeriksa apakah string diakhiri dengan substring tertentu.

```python
name = "Sharleen Aletta"
print(name.endswith("tta"))     # Output: True
print(name.endswith("son"))     # Output: False
```

### len()

Fungsi ini (bukan method) mengembalikan panjang string (jumlah karakter).

```python
name = "Sharleen Aletta"
print(len(name))  # Output: 15
```

### Substring dan Slicing

String dapat diakses seperti list karena string adalah sequence of characters.

```python
name = "Sharleen Aletta"

# Mengambil karakter tunggal
print(name[0])      # Output: S
print(name[5])      # Output: e

# Slicing (potongan string)
print(name[0:8])    # Output: Sharleen
print(name[9:])     # Output: Aletta
print(name[:8])     # Output: Sharleen
print(name[-6:])    # Output: Aletta
print(name[:-1])    # Output: Sharleen Alett (tanpa karakter terakhir)
```

### Operator in

Operator `in` digunakan untuk memeriksa apakah substring ada dalam string.

```python
kata_saya = """Indonesia adalah negara yang indah
berada di bawah garis khatulistiwa
aku cinta Indonesia
"""

print("Indonesia" in kata_saya)  # Output: True
print("Malaysia" in kata_saya)   # Output: False

# Perlu diperhatikan: operator in bersifat case-sensitive
print("indonesia" in kata_saya)  # Output: False
```

## Video Penjelasan

Berikut video penjelasan tentang string dalam Python:

[![String Python](https://img.youtube.com/vi/fhAEh1Z9YuY/0.jpg)](https://www.youtube.com/watch?v=fhAEh1Z9YuY&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=16)

## Hands-On

Berikut adalah contoh program lengkap yang menunjukkan berbagai method string:

```python
name = "Sharleen Aletta"

print("Original name:", name)
print("Upper case:", name.upper())                     # SHARLEEN ALETTA
print("Lower case:", name.lower())                     # sharleen aletta
print("Title case:", name.title())                     # Sharleen Aletta
print("Capitalize:", name.capitalize())                # Sharleen aletta
print("Replace 'Aletta' with 'Smith':", name.replace("Aletta", "Smith"))  # Sharleen Smith
print("Split into list:", name.split())                # ['Sharleen', 'Aletta']
print("Join with '-':", "-".join(name.split()))        # Sharleen-Aletta
print("Find 'Sharleen':", name.find("Sharleen"))       # 0
print("Count 'e':", name.count("e"))                   # 3
print("Starts with 'Shar':", name.startswith("Shar"))  # True
print("Ends with 'tta':", name.endswith("tta"))        # True
print("Length:", len(name))                            # 15
print("First 5 characters:", name[0:5])                # Shar
print("All except last character:", name[:-1])         # Sharleen Alett
print("'Aletta' in name:", "Aletta" in name)           # True
print("'Smith' in name:", "Smith" in name)             # False
```

**[Coba kode String Python](string_python.py)**

## Materi Selanjutnya

<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="../4_operator">[operator] ◀ Materi Sebelumnya</a>
  </div>
  <div>
    <a href="../6_input_output">Materi Selanjutnya ▶ [string]</a>
  </div>
</div>