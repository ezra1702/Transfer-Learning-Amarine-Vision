
# Cara 1. menggunakan dari satu blok 'except'
try:
    teks = "hello"
    angka = int(teks)
    print(angka) # valueError akan terjadi karena teks bukan angka
except ValueError:
    print("Teks tersebut bukan angka")

# Cara 2. menggunakan lebih dari satu blol 'expect'
try:
    print(2/0)
except ZeroDivisionError:
    print("Tidak bisa dibagi nol")
except ValueError:
    print("Teks tersebut bukan angka")

# Cara 3. Menuliskan didalam tupple 
try:
    print(2/0)
except (ZeroDivisionError, ValueError):
    print("Tidak bisa dibagi nol atau teks tersebut bukan angka")

# Cara 4. Menggunakan keyword 'as' untuk memberi nama alias eksepsi
try:
    teks = "hello"
    angka = int(teks)
    print(angka) # valueError akan terjadi karena teks bukan angka
except ValueError as e:
    print(e)

try:
    print(2/0)
except (ZeroDivisionError,TypeError,ValueError) as e:
    print(e)

# Dicoba ke project API

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url, timeout=5)
    print(f"API berhasil dipanggil (status HTTP : {response.raise_for_status()}):\n{response.json()}")
except requests.exceptions.Timeout:
    print("Terjadi timeout saat memanggil API")
except requests.exceptions.HTTPError as e:
    print(f"Terjadi kesalahan HTTP: {e}")
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan dalam permintaan: {e}")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")