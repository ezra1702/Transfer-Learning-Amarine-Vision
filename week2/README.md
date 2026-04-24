## Week 1 — Anaconda Environment Setup dan Dasar GitHub

---

### Deskripsi

Di minggu pertama ini fokusnya bukan langsung coding, tapi **setup pondasi dulu**.

Kenapa penting?  
Karena kalau environment berantakan dari awal:

- library bisa bentrok  
- error susah dilacak  
- project jadi tidak stabil  

Makanya di sini akan setup:

- environment pakai Anaconda  
- workflow Git & GitHub yang benar  

---

### Tujuan Pembelajaran

Setelah menyelesaikan week 1, diharapkan sudah bisa:

- Install dan setup Anaconda dengan benar  
- Membuat dan mengelola virtual environment pakai Conda  
- Install library Python seperti `numpy` dan `opencv-python`  
- Paham konsep dasar Git (version control)  
- Menggunakan perintah Git dasar: `init`, `add`, `commit`, `push`, `pull`  
- Menghubungkan project ke GitHub  

---

### Materi yang Dipelajari

#### 1. Anaconda dan Virtual Environment

Virtual environment itu ibarat **ruang kerja terpisah untuk tiap project**.  
Jadi setiap project punya library sendiri dan tidak saling ganggu.

Kenapa ini penting:

- tidak ada konflik library  
- project lebih rapi  
- gampang di-maintain  

Yang akan dipelajari:

- Cara install Anaconda / Miniconda  
- Perintah dasar Conda: `create`, `activate`, `deactivate`, `install`, `list`  
- Cara manage environment biar tidak tabrakan  
- Export & import environment (`environment.yml`)  

Panduan lengkap ada di:  
[week1/setup/anaconda_setup.md](week1/setup/anaconda_setup.md)

---

#### 2. Git dan GitHub

Git dipakai untuk **melacak semua perubahan code**,  
GitHub dipakai untuk **menyimpan dan kolaborasi**.

Di sini juga akan pakai workflow yang benar (pakai upstream, bukan manual sync).

Yang akan dipelajari:

- Konsep dasar version control  
- Setup awal Git (`git config`)  
- Alur kerja Git: `init → add → commit → push`  
- Cara bikin dan kelola repository di GitHub  
- Perintah penting: `pull`, `clone`, `status`  

Panduan lengkap ada di:  
[week1/setup/git_github.md](week1/setup/git_github.md)

---
#### Struktur Repositries
```
week1-amarine/
├── README.md                      # Dokumentasi utama + opening ramah
├── setup/
│   ├── anaconda_setup.md          # Instalasi & perintah Conda step-by-step
│   └── git_github.md              # Workflow Git: init → add → commit → push
└── assignment/                    # Pengumpulan tugas
    └── nama                       # Untuk Pengumpulan tugas sesuaikan dengan nama (harus buat folde dengan diberikan nama pribadi)
```
