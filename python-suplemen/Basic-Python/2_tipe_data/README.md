<center>

# Tipe Data

</center>
<p align="center">
  <img src="https://preview.redd.it/958mvx20z8371.jpg?auto=webp&s=4aa23a578a4b3d6440f81c5f461eeb4052a6235d">
<p>

<a id="1"><h2>Daftar Isi</h2></a>

- [Pendahuluan](#2)
- [String | `str`](#3)
- [Integer | `int`](#4)
- [Float | `float`](#5)
- [Complex | `complex`](#6)
- [List | `list`](#7)
- [Tuple | `tuple`](#8)
- [Set | `set`](#9)
- [FrozenSet | `frozenset`](#10)
- [Dictionary | `dict`](#11)
- [Bytes | `bytes`](#12)
- [ByteArray | `bytearray`](#13)
- [MemoryView | `memoryview`](#14)
- [Video penjelasan tentang tipe data](#15)
- [Hands-On](#16)

<a id="2"><h2>Pendahuluan</h2></a>

<p style="text-align: justify;"><b>Tipe data</b> merupakan <b>klasifikasi data</b> yang berfungsi untuk menentukan <b>jenis variabel</b> dan <b>operasi</b> yang dapat dilakukan terhadapnya. Dengan menggunakan <b>tipe data</b> yang tepat, komputer dapat <b>menyimpan</b>, <b>mengelola</b>, dan <b>mengolah data</b> secara efisien. Beberapa contoh <b>tipe data</b> yang umum digunakan antara lain <b>integer</b>, <b>float</b>, <b>char</b>, dan <b>string</b>, yang masing-masing memiliki fungsi berbeda dalam pemrograman.</p>

Beberapa tipe data dalam Python:

**Berupa teks**

<a id="3"><h3>String | `str`</h3></a>

Merupakan salah satu tipe data yang berupa string, berfungsi untuk menghasilkan tipe data string seperti huruf abjad atau simbol lain.

```python
nama_saya = "Sharleen"
email_saya = "sharleen@ub.ac.id"
```

**Berupa angka**

<a id="4"><h3>Integer | `int`</h3></a>

Merupakan salah satu tipe numerik yang sering dipakai dalam pemrograman berupa bilangan bulat. Jika diberikan angka yang bukan bulat maka angka di belakang koma tidak ikut.

```python
number = 25
idNumber = 1
```

<a id="5"><h3>Float | `float`</h3></a>

Merupakan salah satu tipe numerik yang menghasilkan bilangan pecahan, sangat berguna dalam menghasilkan nilai secara detail.

```python
kkm = 75.0
nilaiSaya = 100.0
```

<a id="6"><h3>Complex | `complex`</h3></a>

Merupakan salah satu tipe data numerik yang berfungsi menghasilkan sebuah angka kompleks. Contoh angka kompleks bisa dilihat [di sini](https://id.wikipedia.org/wiki/Bilangan_kompleks).

```python
angka_kompleks = 12 + 1j
angkaKompleks = complex(2j)
```

**Berupa urutan (sekuensial)**

<a id="7"><h3>List | `list`</h3></a>

Tipe data list adalah tipe data koleksi yang berisi beberapa nilai yang terdapat dalam satu variabel. List menggunakan kurung kotak `[ ]` dan dapat dimodifikasi sesuai kebutuhan.

```python
# Set list
sharleen = ['manajemen', 22, True]
nilai_siswa = [12, 13, 14]
kelulusan = [True, False, True]

# modifikasi nilai
sharleen[0] = "ekonomi"
```

<a id="8"><h3>Tuple | `tuple`</h3></a>

Tipe data tuple adalah tipe data koleksi yang berisi beberapa nilai yang terdapat dalam satu variabel. Perbedaan di antara keduanya adalah:

- Tipe data tuple jika diberi nilai, maka tipe data tersebut tidak dapat diubah kembali.
- Tipe data tuple menggunakan tutup kurung biasa `()`.

```python
sharleen = ('manajemen', 22, True)
nilai_siswa = (12, 13, 14)
kelulusan = (True, False, True)
```

<a id="9"><h3>Set | `set`</h3></a>

Tipe data set adalah tipe data koleksi yang elemennya dapat diubah, tidak terurut, dan bersifat unik. Sesuai dengan namanya, tipe data set memiliki operasi matematika himpunan seperti gabungan, irisan, selisih, dan lain-lain. Set menggunakan kurung kurawal `{}`. Untuk modifikasi data, set dapat menggunakan metode seperti `add()` untuk menambahkan elemen, `remove()` atau `discard()` untuk menghapus elemen, serta `clear()` untuk menghapus seluruh elemen dalam set.

```python
# Setting set
prodi = {'manajemen', 'teknik nuklir', 'komputer'}
nilai = {12, 13, 14}

# Modifikasi kode
nama_siswa.add("siskom")
nama_siswa.remove("siskom")
```

<a id="10"><h3>FrozenSet | `frozenset`</h3></a>

Tipe data frozenset adalah tipe data koleksi yang mirip dengan set, yang membedakannya dengan set adalah elemen pada frozenset tidak dapat diubah setelah frozenset dibuat.

```python
nama_siswa = frozenset(['woody', 'buzz', 'andy'])
nilai = frozenset([12, 13, 14])
```

**Berupa map (kata kunci, dictionary)**

<a id="11"><h3>Dictionary | `dict`</h3></a>

Tipe data dict atau dictionary adalah tipe data array di mana kunci atau **key** dari array bisa berbentuk string dan angka.

```python
hari = {
    "monday": "senin",
    "tuesday": "selasa",
    "wednesday": "rabu"
}
```

**Berupa tipe data biner (bytes, bytearray, memoryview)**

<a id="12"><h3>Bytes | `bytes`</h3></a>

Merupakan sebuah objek tipe data yang berisikan array tunggal.

```python
number = bytes(12)
number2 = bytes(300)
```

<a id="13"><h3>ByteArray | `bytearray`</h3></a>

Merupakan sebuah objek tipe data yang berisikan array byte tunggal yang tidak dapat diubah.

```python
angka_saya = bytearray(12)
```

<a id="14"><h3>MemoryView | `memoryview`</h3></a>

Memoryview adalah cara aman untuk mengekspos protokol buffer dengan Python. Ini memungkinkan untuk mengakses buffer internal suatu objek dengan membuat objek tampilan. Memoryview mengembalikan fungsi tampilan memori daripada objek yang diberikan.

```python
angka_saya = memoryview(bytes(12))
angka_saya1 = memoryview(bytes(1212))
```

<a id="15"><h2>Video penjelasan tentang tipe data</h2></a>

<center>
<a href="https://youtu.be/ppsCxnNm-JI">
<img src="https://img.youtube.com/vi/ppsCxnNm-JI/hqdefault.jpg"
alt="Data Types in Python" width="600">
</a>
</center>

<a id="16"><h2>Hands-On</h2></a>

Klik link ini untuk mencoba kode Python dari pembahasan kali ini. [Source code](../tipe_data/tipe_data.py)


<div style="display: flex; justify-content: space-between;">
  <div>
    <a href="../1_pendahuluan">[Introduction] ◀ Materi Sebelumnya</a>
  </div>
  <div>
    <a href="../3_variabel">Materi Selanjutnya ▶ [Variable]</a>
  </div>
</div>