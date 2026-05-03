# Setup GitHub dan Instalasi Git

Panduan ini digunakan untuk menyiapkan Git dan GitHub serta alur kontribusi pada proyek Transfer Learning Vision Amarine.

---

# 1. Membuat Akun GitHub

Buka website:
[https://github.com](https://github.com)

Daftarkan akun baru.

Fungsi GitHub:

* Menyimpan repository secara online
* Kolaborasi tim
* Backup project
* Version control

Alasan:

* Semua perubahan tercatat
* Aman untuk kerja tim
* Tidak merusak repository utama

---

# 2. Instalasi Git

## 2.1 Download Git

Buka:
[https://git-scm.com/install/windows](https://git-scm.com/install/windows)

Download versi Windows (64-bit)

---

## 2.2 Instalasi Git

Pilih lokasi instalasi → gunakan default
Alasan: stabil dan direkomendasikan

---

Select Components:

Centang:

* Additional icons → akses cepat
* On the Desktop → shortcut
* Windows Explorer integration → klik kanan Git
* Open Git Bash here → buka terminal langsung
* Open Git GUI here → alternatif GUI
* Git LFS → untuk file besar
* Associate .git* → dikenali sistem
* Associate .sh files → bisa jalankan script
* Add Git Bash ke Windows Terminal → integrasi
* Scalar → performa repo besar

Jangan centang:

* Check daily updates → menghindari notifikasi

---

Default Editor:
Pilih Visual Studio Code

---

Default Branch:
Isi: main

---

PATH:
Pilih:
Git from command line and 3rd-party software

---

SSH:
Pilih:
Use bundled OpenSSH

---

HTTPS Backend:
Pilih:
Windows Secure Channel

---

Terminal:
Pilih:
MinTTY

---

Konfigurasi tambahan:

Centang:

* Fast-forward or merge
* Git Credential Manager
* Enable file system caching

---

## 2.3 Verifikasi

```bash
git --version
```

Jika muncul versi, instalasi berhasil.

---

## 2.4 Konfigurasi Git

```bash
git config --global user.name "Nama"
git config --global user.email "email@gmail.com"
```

Alasan:

* identitas saat commit

---

# 3. Alur Kontribusi GitHub (WAJIB IKUTI)

---

## 3.1 Fork Repository

Fork repository ke akun sendiri

Alasan:

* tidak merusak repository utama

---

## 3.2 Clone Repository

```bash
git clone https://github.com/username/repository.git
cd repository
```

Alasan:

* mengambil project ke lokal

---

## 3.3 Tambahkan Upstream (WAJIB — dilakukan sekali saat awal setelah cloning)

```bash
git remote add upstream https://github.com/original/repository.git
```

Alasan:

* Digunakan **sekali saja saat pertama kali setup setelah cloning repository**
* Menghubungkan repository lokal ke repository utama (owner)
* Memungkinkan update langsung dari terminal tanpa langkah tambahan

Penjelasan:

* Perintah ini hanya dilakukan di awal dan **tidak perlu diulang lagi**
* Setelah dijalankan, koneksi ke repository utama akan tersimpan permanen di project

Penting:

* Dengan menggunakan `upstream`, **tidak perlu menekan tombol "Sync fork" di GitHub**
* Semua proses update dilakukan langsung melalui terminal

## 3.4 WAJIB: Cek Issues Sebelum Mengerjakan

Buka repository utama di GitHub → masuk ke tab **Issues**

Pilih issue yang akan dikerjakan.

Alasan:

* memastikan tugas yang dikerjakan jelas
* menghindari duplikasi pekerjaan dengan orang lain
* mengikuti kebutuhan project

---

## 3.5 Update Repository (WAJIB sebelum mulai kerja)

```bash
git status
git checkout main
git pull upstream main
git push origin main
````

Penjelasan:

* `git status` → memastikan tidak ada perubahan atau conflict (HARUS clean)
* `git checkout main` → pindah ke branch utama
* `git pull upstream main` → ambil update terbaru dari repository utama
* `git push origin main` → sinkronkan ke repository sendiri (fork)

Alasan:

* memastikan repository dalam kondisi bersih sebelum update
* menghindari conflict saat mengambil perubahan terbaru
* memastikan menggunakan versi terbaru dari owner
* menjaga sinkronisasi antara local, upstream, dan origin

---

## 3.6 Buat Branch Baru

```bash
git checkout -b [branch-sendiri]
```

Alasan:

* tidak bekerja langsung di main
* memisahkan pekerjaan
* Setiap melakukan pekerjaan, buat branch baruuu yang berbeda - beda

---

## 3.7 Kerjakan Tugas

Lakukan perubahan sesuai issue yang dipilih.

---

## 3.8 Commit Perubahan

```bash
git add .
git commit -m "menyelesaikan issue"
```

Alasan:

* menyimpan perubahan
* mencatat riwayat kerja

---

## 3.9 Push ke GitHub

```bash
git push origin [branch-sendiri]
```

Alasan:

* mengirim hasil kerja ke repository GitHub

---

## 3.10 Pull Request

Buka GitHub → klik "Compare & Pull Request"

Alasan:

* mengajukan perubahan ke repository utama
* dilakukan review sebelum digabung
