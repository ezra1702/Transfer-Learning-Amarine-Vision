#  Panduan Git & GitHub — Workflow Dasar

Dokumen ini memandu kamu memahami dan mempraktikkan alur kerja Git & GitHub dari awal hingga repository pertama kamu berhasil di-*push*.

---

## Apa itu Git & GitHub?

| Konsep | Penjelasan |
|--------|-----------|
| **Git** | Sistem version control lokal yang mencatat setiap perubahan kode di komputermu |
| **GitHub** | Platform cloud untuk menyimpan dan berbagi repository Git secara online |
| **Repository (Repo)** | Folder proyek yang dikelola oleh Git |
| **Commit** | "Snapshot" dari perubahan kode pada satu waktu tertentu |
| **Branch** | Cabang pengembangan yang independen |
| **Remote** | Versi repository yang ada di server (GitHub) |

---

##  1. Instalasi Git

### Windows
Download di [https://git-scm.com/download/win](https://git-scm.com/download/win) dan jalankan installer.

### macOS
```bash
# Menggunakan Homebrew
brew install git

# Atau cukup jalankan perintah ini, macOS akan meminta instalasi otomatis
git --version
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install git -y
```

### Verifikasi
```bash
git --version
# Output: git version 2.x.x
```

---

##  2. Konfigurasi Awal Git

Lakukan konfigurasi ini **sekali saja** setelah instalasi Git:

```bash
# Set nama pengguna (gunakan nama aslimu)
git config --global user.name "Nama Lengkapmu"

# Set email (gunakan email yang sama dengan akun GitHub)
git config --global user.email "emailmu@example.com"

# Set editor default (opsional, VS Code direkomendasikan)
git config --global core.editor "code --wait"

# Atur branch default bernama 'main'
git config --global init.defaultBranch main

# Verifikasi konfigurasi
git config --list
```

---

##  3. Membuat Repository di GitHub

1. Buka [https://github.com](https://github.com) dan login
2. Klik tombol **"New"** atau **"+"** di pojok kanan atas
3. Isi informasi repository:
   - **Repository name:** `week1-amarine`
   - **Description:** `Week 1 - Anaconda Environment Setup and Basic GitHub`
   - **Visibility:** Public
   -  Jangan centang "Initialize this repository with a README"
4. Klik **"Create repository"**
5. Salin URL repository (format: `https://github.com/username/week1-amarine.git`)

---

##  4. Alur Kerja Git Lengkap

### Langkah 1 — Inisialisasi Repository Lokal

```bash
# Buat folder proyek
mkdir week1-amarine
cd week1-amarine

# Inisialisasi Git di folder ini
git init

# Output: Initialized empty Git repository in .../week1-amarine/.git/
```

### Langkah 2 — Buat File Pertama

```bash
# Buat file README sederhana
echo "# Week 1 - Amarine" > README.md

# Cek status repository
git status
# Output: README.md muncul sebagai "Untracked files"
```

### Langkah 3 — Staging (git add)

```bash
# Tambahkan file tertentu ke staging area
git add README.md

# Atau tambahkan SEMUA perubahan sekaligus
git add .

# Cek status lagi
git status
# Output: README.md muncul sebagai "Changes to be committed"
```

>  **Staging area** adalah tempat "antrian" sebelum perubahan disimpan sebagai commit.

### Langkah 4 — Commit

```bash
# Simpan perubahan dengan pesan yang deskriptif
git commit -m "feat: tambah README.md awal"

# Output:
# [main (root-commit) abc1234] feat: tambah README.md awal
# 1 file changed, 1 insertion(+)
```

>  **Tips commit message:** Gunakan format `tipe: deskripsi singkat`
> - `feat:` untuk fitur baru
> - `fix:` untuk perbaikan bug
> - `docs:` untuk perubahan dokumentasi
> - `chore:` untuk maintenance

### Langkah 5 — Hubungkan ke GitHub (Remote)

```bash
# Tambahkan remote origin (ganti URL dengan milikmu)
git remote add origin https://github.com/username/week1-amarine.git

# Verifikasi remote
git remote -v
# Output:
# origin  https://github.com/username/week1-amarine.git (fetch)
# origin  https://github.com/username/week1-amarine.git (push)
```

### Langkah 6 — Push ke GitHub

```bash
# Push branch main ke GitHub (-u untuk set upstream)
git push -u origin main

# Setelah pertama kali, cukup gunakan:
git push
```

---

## 5. Perintah Git yang Sering Digunakan

### Melihat Status & Riwayat

```bash
# Cek status perubahan
git status

# Lihat riwayat commit
git log

# Lihat riwayat commit (ringkas, satu baris)
git log --oneline

# Lihat perubahan yang belum di-stage
git diff

# Lihat perubahan yang sudah di-stage
git diff --staged
```

### Mengambil Perubahan dari GitHub

```bash
# Ambil perubahan terbaru dari remote
git pull

# Sama dengan (git fetch + git merge)
git fetch origin
git merge origin/main
```

### Clone Repository

```bash
# Clone repository orang lain atau milikmu di komputer baru
git clone https://github.com/username/week1-amarine.git

# Clone ke folder dengan nama tertentu
git clone https://github.com/username/week1-amarine.git nama-folder
```

### Membatalkan Perubahan

```bash
# Batalkan perubahan pada file sebelum di-stage
git restore nama-file.py

# Batalkan staging (kembalikan ke unstaged)
git restore --staged nama-file.py

# Kembali ke commit tertentu (HATI-HATI: destruktif)
git reset --hard abc1234
```

---

##  6. Dasar-dasar Branch

```bash
# Lihat semua branch
git branch

# Buat branch baru
git branch nama-branch

# Pindah ke branch lain
git checkout nama-branch

# Buat dan langsung pindah ke branch baru
git checkout -b nama-branch

# Merge branch ke main
git checkout main
git merge nama-branch
```

---


##  Diagram Alur Kerja Git

```
Working Directory  →  Staging Area  →  Local Repo  →  Remote (GitHub)
      |                    |                |                |
   (edit file)          git add           git commit      git push
                           |                |                |
                      git restore     git log          git pull (balik)
```

---
