# Analisis Kualitas Udara dengan NumPy dan pandas

Project ini merangkum bagian NumPy dan pandas dari Module 4 course Introduction to Data Analysis Using Python (Google Data Analytics Professional Certificate). Latihan dijalankan ulang dari awal sampai akhir lewat satu script: `analyze_aqi.py`.

## Materi yang dipelajari

1. NumPy: membuat array, statistik ringkas (mean, min, max, std), dan persentase pembacaan terbersih
2. pandas: membaca CSV, info dan describe, value counts, sorting, iloc, boolean masking, groupby, dan concat

## Dataset

Data indeks kualitas udara (AQI) dari EPA Amerika Serikat:

* `epa_ca_tx_pa.csv`: 546 pembacaan dari California, Texas, dan Pennsylvania
* `epa_others.csv`: 1179 pembacaan dari state lainnya

Nilai AQI berjalan dari 0 sampai 500. Nilai 50 ke bawah berarti kualitas udara baik, nilai di atas 300 berarti berbahaya.

## Cara menjalankan

```bash
python analyze_aqi.py
```

Script akan mencetak semua hasil latihan, menyimpan 4 chart di folder `charts/`, dan menulis ringkasan angka di `findings.json`.

## Hasil utama

* Rata rata AQI 8.91; 99.63 persen pembacaan termasuk kategori bersih (AQI 50 ke bawah)
* AQI tertinggi 93 tercatat di Los Angeles, California; rata rata AQI Los Angeles 13.4
* Rata rata AQI per state: California 9.41, Texas 9.38, Pennsylvania 6.69
* Setelah digabung, total 1725 baris; 4 baris Washington punya AQI 51 ke atas

## Struktur folder

* `analyze_aqi.py`: script utama berisi semua latihan
* `charts/`: 4 visualisasi hasil analisis
* `data/`: kedua file CSV asli dari course
* `findings.json`: ringkasan angka hasil eksekusi
