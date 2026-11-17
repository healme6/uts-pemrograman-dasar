from inventaris_pkg.file_handler import baca_csv, simpan_json
from inventaris_pkg.processor import (
    bersihkan_dan_validasi,
    cari_barang,
    filter_stok_menipis,
    hitung_rekap_kategori,
)
from inventaris_pkg.reporter import buat_struktur_laporan, tampilkan_tabel


def main():
    """Fungsi utama pengendali antarmuka command line aplikasi."""
    path_input = "data/input_inventaris.csv"
    path_output = "data/output_laporan.json"

    print("=== APLIKASI PENGOLAHAN DATA INVENTARIS ===")
    ubah_path = input(f"Gunakan file default ({path_input})? [y/n]: ").strip().lower()
    if ubah_path == "n":
        path_input = input("Masukkan path file CSV: ").strip()

    try:
        data_mentah = baca_csv(path_input)
    except (FileNotFoundError, ValueError, OSError) as err:
        print(f"Gagal memuat data: {err}")
        return

    data_bersih, jumlah_rusak = bersihkan_dan_validasi(data_mentah)
    print(f"Data dimuat. Valid: {len(data_bersih)} item, Diabaikan (duplikat/rusak): {jumlah_rusak} baris.")

    while True:
        print("\nMenu Utama:")
        print("1. Tampilkan semua inventaris bersih")
        print("2. Cari barang berdasarkan nama")
        print("3. Filter barang dengan stok menipis")
        print("4. Lihat rekapitulasi aset per kategori")
        print("5. Simpan laporan analisis ke JSON")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_tabel(data_bersih)
        elif pilihan == "2":
            kata = input("Masukkan nama barang yang dicari: ")
            hasil = cari_barang(data_bersih, kata)
            tampilkan_tabel(hasil)
        elif pilihan == "3":
            try:
                batas_input = input("Masukkan batas maksimal stok (default 5): ").strip()
                batas = int(batas_input) if batas_input else 5
                if batas < 0:
                    print("Batas stok tidak boleh negatif.")
                    continue
                menipis = filter_stok_menipis(data_bersih, batas)
                tampilkan_tabel(menipis)
            except ValueError:
                print("Input tidak valid. Masukkan angka bulat.")
        elif pilihan == "4":
            rekap = hitung_rekap_kategori(data_bersih)
            print("\n--- REKAPITULASI ASET PER KATEGORI ---")
            for kat, nilai in rekap.items():
                print(f"- {kat}: Rp {nilai:,.0f}")
            total = sum(rekap.values())
            print(f"Total Keseluruhan Aset: Rp {total:,.0f}")
        elif pilihan == "5":
            rekap = hitung_rekap_kategori(data_bersih)
            menipis = filter_stok_menipis(data_bersih, 5)
            laporan = buat_struktur_laporan(data_bersih, rekap, menipis, jumlah_rusak)
            try:
                simpan_json(path_output, laporan)
                print(f"Laporan berhasil disimpan ke {path_output}")
            except OSError as err:
                print(f"Gagal menyimpan file JSON: {err}")
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak tersedia. Silakan pilih angka 0 sampai 5.")


if __name__ == "__main__":
    main()
