# Transfer Learning — Amarine Vision

**Program Studi:** Teknik Informatika  
**Mata Kuliah:** Transfer Learning (Computer Vision)  
**Institusi:** Amarine  
**Status:** Aktif — Minggu ke-1 dari 8

---

## Tentang Kuliah Ini

Kuliah Transfer Learning Amarine Vision dirancang untuk membekali mahasiswa dengan kemampuan praktis dalam bidang computer vision menggunakan pendekatan transfer learning. Selama program berlangsung, mahasiswa akan belajar mulai dari persiapan lingkungan kerja, pemahaman dasar computer vision, hingga implementasi model deep learning pada kasus nyata.

Seluruh materi, tugas, dan dokumentasi dikelola melalui repositori GitHub ini. Pastikan kamu sudah bergabung dan memahami cara menggunakannya sebelum memulai.

---

## Daftar Minggu

| Minggu | Topik | Status |
|--------|-------|--------|
| Week 1 | Anaconda Environment Setup dan Dasar GitHub | Aktif |
| Week 2 | Dasar-Dasar Python untuk Computer Vision | Akan Datang |
| Week 3 | Pengenalan OpenCV dan Pengolahan Citra | Akan Datang |
| Week 4 | Deep Learning dan Convolutional Neural Network | Akan Datang |
| Week 5 | Transfer Learning: Konsep dan Arsitektur | Akan Datang |
| Week 6 | Fine-Tuning Model pada Dataset Kustom | Akan Datang |
| Week 7 | Evaluasi Model dan Visualisasi Hasil | Akan Datang |
| Week 8 | Proyek Akhir dan Presentasi | Akan Datang |

---

## Week 1 — Anaconda Environment Setup dan Dasar GitHub

### Deskripsi

Minggu pertama ini berfokus pada persiapan. Sebelum bisa menulis satu baris pun kode machine learning, kamu perlu memiliki lingkungan kerja yang rapi dan terkontrol. Di sinilah peran Anaconda dan Git menjadi sangat penting.

Anaconda membantu kamu membuat environment Python yang terisolasi, sehingga setiap proyek tidak saling mengganggu. Git dan GitHub memungkinkan kamu menyimpan, melacak, dan berbagi kode secara profesional — keterampilan yang wajib dimiliki oleh siapapun yang bekerja di bidang teknologi.

Jangan anggap remeh minggu ini. Fondasi yang kuat di sini akan membuat seluruh perjalanan belajarmu jauh lebih lancar.

---

### Tujuan Pembelajaran

Setelah menyelesaikan materi week 1, kamu diharapkan mampu:

- Menginstal dan mengonfigurasi Anaconda di sistem operasi masing-masing
- Membuat dan mengelola virtual environment Python menggunakan Conda
- Menginstal library Python yang dibutuhkan seperti numpy dan opencv-python
- Memahami konsep dasar version control menggunakan Git
- Melakukan operasi Git fundamental: `init`, `add`, `commit`, `push`, dan `pull`
- Menghubungkan repository lokal ke GitHub

---

### Materi yang Dipelajari

#### 1. Anaconda dan Virtual Environment

Virtual environment adalah cara untuk membuat "ruang kerja" Python yang terpisah untuk setiap proyek. Bayangkan seperti memiliki laptop berbeda untuk setiap tugas — tidak ada library yang saling tabrakan.

- Instalasi Anaconda
- Perintah dasar Conda: `create`, `activate`, `deactivate`, `install`, `list`
- Manajemen environment untuk proyek yang terisolasi
- Export dan import environment menggunakan `environment.yml`

Panduan lengkap instalasi Anaconda tersedia di: [week1/setup/anacond_setup.md](week1/setup/anacond_setup.md)

---

#### 2. Git dan GitHub

Git adalah sistem untuk melacak perubahan kode. GitHub adalah tempat menyimpan kode tersebut secara online. Keduanya adalah standar industri yang digunakan di perusahaan teknologi seluruh dunia.

- Konsep dasar version control
- Konfigurasi awal Git menggunakan `git config`
- Alur kerja Git: `init` → `add` → `commit` → `push`
- Membuat dan mengelola repository di GitHub
- Perintah `pull`, `clone`, dan `status`

Panduan lengkap penggunaan Git dan GitHub tersedia di: [week1/setup/git_github.md](week1/setup/git_github.md)

---

### Tools yang Digunakan

| Tool | Versi | Fungsi |
|------|-------|--------|
| [Anaconda](https://www.anaconda.com/) | Latest | Manajemen environment Python |
| [Python](https://www.python.org/) | 3.10 ke atas | Bahasa pemrograman utama |
| [Git](https://git-scm.com/) | 2.x | Version control system |
| [GitHub](https://github.com/) | — | Platform hosting repository |
| [VS Code](https://code.visualstudio.com/) | Latest | Code editor (opsional) |
| NumPy | 1.24 ke atas | Library komputasi numerik |
| OpenCV | 4.x | Library computer vision |

---

### Perintah Conda yang Wajib Diingat

Berikut adalah perintah-perintah Conda yang akan sering kamu gunakan selama kuliah ini.

```bash
# Membuat environment baru
conda create -n amarine-vision python=3.10

# Mengaktifkan environment
conda activate amarine-vision

# Menginstal library
conda install numpy
pip install opencv-python

# Melihat daftar environment yang ada
conda env list

# Menonaktifkan environment
conda deactivate
```

---

### Alur Kerja Git Dasar

Berikut adalah urutan perintah Git yang akan kamu gunakan setiap kali menyimpan pekerjaan ke GitHub.

```bash
# Inisialisasi repository (hanya sekali di awal)
git init

# Menambahkan file ke staging
git add .

# Menyimpan perubahan dengan pesan
git commit -m "Tulis pesan perubahan di sini"

# Mengirim ke GitHub
git push origin main
```

---

### Struktur Repositori Week 1

```
week1/
├── README.md                   # Dokumentasi detail week 1
└── setup/
    ├── anacond_setup.md        # Instalasi dan perintah Conda step-by-step
    └── git_github.md           # Workflow Git: init → add → commit → push
```

---

### Tugas Week 1

Tugas minggu pertama adalah membuktikan bahwa kamu sudah berhasil menyiapkan lingkungan kerja dengan benar. Caranya:

1. Instal Anaconda dan buat environment bernama `amarine-vision`
2. Instal library `numpy` dan `opencv-python` di dalam environment tersebut
3. Buat akun GitHub jika belum punya
4. Fork atau clone repositori ini ke komputer kamu
5. Buat folder dengan nama kamu di dalam direktori `week1/`
6. Tambahkan file `README.md` singkat di dalam folder tersebut yang berisi nama, NIM, dan screenshot environment yang sudah aktif
7. Commit dan push ke GitHub

Pengumpulan dilakukan melalui pull request ke repositori ini sebelum batas waktu yang ditentukan.

---

## Aturan Umum

- Seluruh tugas dikumpulkan melalui GitHub sesuai struktur yang telah ditentukan
- Penamaan folder dan file harus konsisten dan menggunakan huruf kecil dengan tanda hubung sebagai pemisah kata
- Commit message ditulis dengan jelas, menggambarkan apa yang diubah
- Plagiarisme dalam bentuk apapun tidak ditoleransi
- Jika ada pertanyaan, ajukan melalui channel diskusi yang telah disediakan

---

## Cara Berkontribusi ke Repositori Ini

1. Fork repositori ini ke akun GitHub kamu
2. Clone hasil fork ke komputer lokal
3. Buat folder dengan nama kamu di dalam folder week yang sesuai
4. Tambahkan file dan commit perubahan
5. Push ke GitHub dan buat pull request

```bash
git clone https://github.com/username/Transfer-Learning-Amarine-Vision.git
cd Transfer-Learning-Amarine-Vision
git checkout -b nama-kamu/week1
# ... buat perubahan ...
git add .
git commit -m "Tambah tugas week 1 - Nama Kamu"
git push origin nama-kamu/week1
```

---

## Kontak dan Dukungan

Jika kamu mengalami kendala teknis atau memiliki pertanyaan seputar materi, hubungi pengajar melalui platform komunikasi yang sudah disepakati di kelas. Hindari mengirim pesan di luar jam kerja yang ditentukan.

---

*Repositori ini dikelola oleh tim pengajar Transfer Learning Amarine Vision.*  
*Terakhir diperbarui: April 2026*
