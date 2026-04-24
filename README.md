# Roadmap Vision Amarine (April - September 2026)

Dokumen ini merupakan panduan pembelajaran terstruktur dalam bidang Computer Vision dan Deep Learning yang dirancang secara bertahap, mulai dari tahap pengenalan hingga implementasi pada sistem nyata.

Seluruh rangkaian materi difokuskan pada keseimbangan antara konsep teoritis dan praktik langsung, sehingga proses pembelajaran tidak hanya memahami dasar, tetapi juga mampu membangun, melatih, dan mengimplementasikan model secara mandiri.

Cakupan pembelajaran meliputi:

* Kurikulum mingguan yang disusun progresif dari level dasar ke lanjutan
* Aktivitas berbasis praktik untuk memperkuat pemahaman
* Pengolahan dataset serta teknik preprocessing
* Proses training model dan optimasi performa
* Implementasi model ke dalam sistem berbasis aplikasi, edge device, dan IoT

Dokumen ini diharapkan dapat menjadi acuan dalam mengembangkan kemampuan di bidang Computer Vision secara sistematis dan berkelanjutan.

---

## Target Akhir

* Membangun model YOLO menggunakan dataset kustom
* Melakukan deteksi objek secara real-time dengan hasil yang stabil
* Menguasai tools seperti OpenCV, CNN, YOLO, ROS 2, dan Jetson Orin
* Mampu melakukan deployment model ke sistem edge maupun cloud

---

# Quick Navigation Table
---

# Quick Navigation Table

| Week  | Topic                             | Navigation          | Detail Materi                                                                                      | Status      |
| ----- | --------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------- | ----------- |
| 1     | Bonding & Introduction to Vision  | [Go to Week 1](week1/README.md) | Pengenalan Vision Amarine, gambaran pembelajaran, serta diskusi dasar computer vision              | Done        |
| Bonus | Basic Python + OOP                | [Bonus Week](python-suplemen/objek_oriented_programming/) | Dasar Python, control flow, serta konsep OOP seperti class, object, inheritance, dan encapsulation | Done        |
| 2     | Python Environment & Basic GitHub | [Go to Week 2](week2/README.md) | Setup Python environment serta penggunaan dasar GitHub (commit, push, pull)                        | Done        |
| 3     | Fundamental Computer Vision       | -                   | Implementasi dasar computer vision menggunakan Python dan OpenCV                                   | -           |
| 4     | Neural Network & Optimization     | -                   | TensorFlow, PyTorch, serta teknik optimasi model                                                   | -           |
| 5     | Dataset Creation & Preprocessing  | -                   | Pembuatan dataset, labeling, augmentasi, dan pembagian data                                        | -           |
| 6     | Introduction to YOLO              | -                   | Dasar YOLO, arsitektur, serta parameter awal                                                       | -           |
| Break | Academic Break                    | -                   | Penguatan materi Week 3 hingga Week 6                                                              | -           |
| 7     | Deep Dive YOLO                    | -                   | Training dengan dataset kustom dan evaluasi model                                                  | -           |
| 8     | ROS 2 Integration                 | -                   | Integrasi YOLO dengan ROS 2 dan sistem robotik                                                     | -           |
| 9     | EDA & Streamlit Deployment        | -                   | Analisis dataset dan pembuatan dashboard                                                           | -           |
| 10    | Model Optimization                | -                   | Hyperparameter tuning, pruning, dan quantization                                                   | -           |
| 11    | Explainable AI                    | -                   | Grad-CAM, SHAP, dan analisis interpretasi model                                                    | -           |
| 12    | Edge Deployment & IoT             | -                   | Deployment ke edge device dan integrasi IoT                                                        | -           |
| 13    | Final Project                     | -                   | Integrasi model ke edge dan cloud system                                                           | -           |

---

## Panduan Penggunaan

* Status hanya diperbarui oleh penanggung jawab utama
* Progress individu dapat dilihat melalui milestone repository
* Navigation digunakan untuk mengakses detail tiap minggu
* Folder berisi materi dan implementasi kode
* Struktur timeline menyesuaikan kalender akademik

---

## Week 1: Introduction & Setup

Materi:

* Penjelasan alur pembelajaran
* Pengenalan tools dan framework
* Dasar Computer Vision

Studi Kasus:

* Diskusi peluang dan tantangan dalam bidang visi komputer

Praktik:

* Instalasi dan konfigurasi environment

---

## Bonus Week: Basic Python & OOP

Materi:

* Struktur dasar Python
* Control flow dan fungsi
* Konsep OOP: class, object, inheritance, encapsulation

---

## Week 2: Numerical Analysis

Materi:

* Penggunaan NumPy
* Visualisasi dengan Matplotlib

Studi Kasus:

* Pengolahan dan visualisasi data sederhana

Praktik:

* Implementasi analisis numerik

---

## Week 3: Fundamental Computer Vision

Materi:

* Dasar pengolahan citra
* Penggunaan OpenCV

Studi Kasus:

* Implementasi deteksi sederhana

---

## Week 4: Neural Network

Materi:

* Convolutional layer
* Pooling layer
* Activation function
* Fully connected layer

Studi Kasus:

* Klasifikasi menggunakan dataset Fashion MNIST

Praktik:

* Training model CNN

---

## Week 5: Dataset & Preprocessing

Materi:

* Pembuatan dataset
* Labeling dan anotasi
* Augmentasi data
* Pembagian dataset

Studi Kasus:

* Perbandingan hasil sebelum dan sesudah augmentasi

Praktik:

* Membuat dataset sendiri

---

## Week 6: Introduction to YOLO

Materi:

* Konsep YOLO
* Struktur model
* Parameter dasar

Studi Kasus:

* Deteksi objek menggunakan dataset umum

Praktik:

* Eksperimen parameter

---

## Week 7: Deep Dive YOLO

Materi:

* Integrasi dataset kustom
* Training lanjutan

Studi Kasus:

* Object detection

Praktik:

* Perbandingan hasil model

---

## Week 8: ROS 2 Integration

Materi:

* Alur kerja ROS 2
* Integrasi dengan YOLO

Studi Kasus:

* Implementasi pada sistem robot

Praktik:

* Pipeline komunikasi

---

## Week 9: EDA & Deployment

Materi:

* Exploratory Data Analysis
* Data cleaning
* Visualisasi

Studi Kasus:

* Analisis dataset

Praktik:

* Dashboard Streamlit

---

## Week 10: Optimization

Materi:

* Hyperparameter tuning
* Transfer learning
* Pruning dan quantization

Studi Kasus:

* Optimasi performa model

---

## Week 11: Explainable AI

Materi:

* Konsep XAI
* Grad-CAM
* SHAP

Studi Kasus:

* Analisis bias model

---

## Week 12: Edge & IoT

Materi:

* Konversi model
* Deployment ke edge device
* Real-time inference

Studi Kasus:

* Implementasi pada sistem nyata

Praktik:

* Sistem notifikasi

---

# Final Project

Target:

* Penyelesaian model
* Deployment ke edge dan cloud
* Monitoring sistem

Praktik:

* Dashboard monitoring
* Integrasi database

---

## Referensi

* OpenCV Documentation
* YOLO Ultralytics
* TensorFlow CNN Guide
* ROS 2 Documentation
* Explainable AI Resources

---
