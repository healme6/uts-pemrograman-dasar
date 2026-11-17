# Aplikasi CLI Pengolahan Data Inventaris Barang

## Deskripsi
Aplikasi berbasis command line (CLI) menggunakan Python untuk membaca data inventaris dari file CSV, membersihkan duplikasi serta data tidak valid, menganalisis stok menipis, dan mengekspor laporan rekapitulasi aset ke format JSON.

## Struktur Proyek
- `main.py` : Titik masuk utama program (antarmuka CLI)
- `inventaris_pkg/__init__.py` : Inisialisasi package
- `inventaris_pkg/file_handler.py` : Modul pembacaan CSV dan penulisan JSON
- `inventaris_pkg/processor.py` : Modul validasi, filter, pencarian, dan kalkulasi
- `inventaris_pkg/reporter.py` : Modul pemformatan tabel terminal dan struktur laporan
- `data/input_inventaris.csv` : Contoh data mentah inventaris
- `data/output_laporan.json` : Hasil ekspor laporan analisis

## Dependency dan Persyaratan Sistem
- Python versi 3.8 atau lebih baru
- Hanya menggunakan Python Standard Library (`csv`, `json`, `os`) tanpa library eksternal

## Cara Menjalankan Aplikasi
1. Buka terminal dan arahkan ke direktori utama proyek (`uts_inventaris`):
   ```bash
   cd uts_inventaris
   ```
2. Jalankan perintah:
   ```bash
   python main.py
   ```
3. Tekan `y` saat diminta menggunakan file default `data/input_inventaris.csv`.
4. Pilih angka `1` sampai `5` untuk mencoba fitur, lalu pilih `5` untuk menghasilkan file `data/output_laporan.json`.
