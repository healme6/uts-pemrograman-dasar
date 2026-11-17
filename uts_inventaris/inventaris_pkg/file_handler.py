import csv
import json
import os


def baca_csv(path_file):
    """Membaca file CSV dan mengembalikan list berisi dictionary per baris."""
    if not os.path.exists(path_file):
        raise FileNotFoundError(f"File tidak ditemukan: {path_file}")

    hasil = []
    with open(path_file, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        kolom_wajib = {"kode_barang", "nama_barang", "kategori", "stok", "harga_satuan"}
        if not reader.fieldnames or not kolom_wajib.issubset(set(reader.fieldnames)):
            raise ValueError("Format header CSV tidak sesuai standar.")

        for baris in reader:
            hasil.append(dict(baris))
    return hasil


def simpan_json(path_file, data):
    """Menyimpan data dictionary ke dalam file berformat JSON."""
    folder = os.path.dirname(path_file)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    with open(path_file, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return True
