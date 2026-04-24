# Instalasi dan Penggunaan Anaconda untuk Transfer Learning Vision Amarine

## 1. Latar Belakang

Dalam pengembangan proyek **Transfer Learning Vision Amarine**, pengelolaan dependensi dan lingkungan kerja menjadi hal yang sangat penting.

Jika hanya menggunakan Python secara langsung tanpa manajemen environment, beberapa masalah yang sering muncul antara lain:

* Konflik versi library antar proyek
* Kesulitan dalam mengelola dependensi
* Instalasi library yang tidak stabil, terutama untuk kebutuhan machine learning

Untuk mengatasi hal tersebut, digunakan **Anaconda** atau **Miniconda**.

Keunggulan penggunaan Anaconda/Miniconda:

* Mendukung pembuatan environment terpisah untuk setiap proyek
* Mempermudah instalasi dan pengelolaan library
* Menghindari konflik antar dependensi
* Lebih stabil untuk pengembangan proyek Transfer Learning Vision Amarine

Kesimpulan:
Penggunaan Anaconda atau Miniconda sangat direkomendasikan untuk menjaga kestabilan dan kerapian proyek.

---

## 2. Instalasi Anaconda / Miniconda

### 2.1 Download

Buka website resmi:
[https://www.anaconda.com](https://www.anaconda.com)

Pilih:

* Miniconda (versi ringan)
  alasannya : 
  - Ukuran instalasi lebih kecil dan ringan
  - Tidak membawa banyak library bawaan yang belum tentu digunakan
  - Lebih fleksibel karena dependensi dapat diinstall sesuai kebutuhan proyek
  - Cocok untuk pengembangan bertahap seperti pada Transfer Learning Vision Amarine
  - Lebih optimal digunakan bersama Visual Studio Code karena environment dapat dikontrol secara spesifik
---

### 2.2 Proses Instalasi

#### a. Pemilihan tipe instalasi

Pilih:
**Just Me (recommended)**

Alasan:

* Tidak memerlukan hak akses administrator
* Lebih aman untuk penggunaan pribadi
* Mengurangi potensi error

---

#### b. Lokasi instalasi

Gunakan lokasi default yang disediakan installer.

---

#### c. Advanced Installation Options

Pilih opsi berikut:

* Create shortcuts
* Register Anaconda as my default Python
* Clear the package cache

Jangan memilih:

* Add Anaconda to PATH environment variable

Penjelasan:

* Create shortcuts: mempermudah akses aplikasi
* Register default Python: memastikan Python dari Anaconda digunakan oleh sistem dan IDE
* Clear cache: menghemat ruang penyimpanan
* Add to PATH: dapat menyebabkan konflik dengan instalasi Python lain

---

### 2.3 Menyelesaikan instalasi

Tunggu hingga proses instalasi selesai, kemudian lanjutkan ke tahap konfigurasi.

---

## 3. Konfigurasi Terminal

### 3.1 Inisialisasi Conda

Buka Anaconda Prompt, lalu jalankan perintah berikut:

```bash
conda init powershell
conda init cmd.exe
conda init bash
```

Penjelasan:

* powershell: untuk PowerShell
* cmd.exe: untuk Command Prompt
* bash: untuk Git Bash atau WSL

Setelah itu, tutup dan buka kembali terminal atau aplikasi seperti Visual Studio Code.

---

### 3.2 Verifikasi instalasi

Jalankan perintah:

```bash
conda --version
```

Jika versi conda muncul, maka instalasi berhasil.

---

## 4. Penggunaan Dasar Anaconda

### 4.1 Membuat environment baru

Environment digunakan agar dependensi proyek tidak bercampur dengan proyek lain.

Contoh:

```bash
conda create -n TL-Amarine-Vision python=3.10
```

---

### 4.2 Mengaktifkan environment

```bash
conda activate TL-Amarine-Vision
```

---

### 4.3 Menginstal library

```bash
conda install numpy pandas matplotlib
```

Untuk kebutuhan Transfer Learning Vision Amarine:

```bash
pip install torch torchvision
```

---

### 4.4 Menghapus library

```bash
conda remove numpy
```

---

### 4.5 Menghapus environment

```bash
conda remove -n TL-Amarine-Vision --all
```

---

## 5. Integrasi dengan Visual Studio Code

Untuk menggunakan Anaconda di VS Code:

1. Install extension:

   * Python
   * Pylance

2. Pilih interpreter:

   * Tekan Ctrl + Shift + P
   * Pilih: Python: Select Interpreter

3. Pilih environment:

   * TL-Amarine-Vision (conda)

---
#### Struktur Repositries
```
week2-amarine/
├── README.md                      # Dokumentasi utama + opening ramah
├── setup/
│   ├── anaconda_setup.md          # Instalasi & perintah Conda step-by-step
│   └── git_github.md              # Workflow Git: init → add → commit → push
└── assignment/                    # Pengumpulan tugas
    └── nama                       # Untuk Pengumpulan tugas sesuaikan dengan nama (harus buat folde dengan diberikan nama pribadi)
```
