def tampilkan_tabel(daftar_barang):
    """Menampilkan daftar barang dalam format tabel rapi di terminal."""
    if not daftar_barang:
        print("Tidak ada data barang untuk ditampilkan.")
        return

    garis = "-" * 78
    print(garis)
    print(f"{'KODE':<8} | {'NAMA BARANG':<28} | {'KATEGORI':<13} | {'STOK':>5} | {'HARGA':>12}")
    print(garis)
    for b in daftar_barang:
        print(
            f"{b['kode_barang']:<8} | "
            f"{b['nama_barang'][:28]:<28} | "
            f"{b['kategori'][:13]:<13} | "
            f"{b['stok']:>5} | "
            f"{b['harga_satuan']:>12,.0f}"
        )
    print(garis)


def buat_struktur_laporan(data_bersih, rekap_kategori, stok_menipis, jumlah_rusak):
    """Menyusun struktur dictionary laporan akhir untuk diekspor ke JSON."""
    total_aset = sum(b["total_nilai"] for b in data_bersih)
    return {
        "ringkasan": {
            "total_jenis_barang_valid": len(data_bersih),
            "total_baris_diabaikan": jumlah_rusak,
            "total_nilai_aset_keseluruhan": total_aset,
            "jumlah_barang_stok_menipis": len(stok_menipis)
        },
        "rekap_aset_per_kategori": rekap_kategori,
        "peringatan_stok_menipis": stok_menipis,
        "daftar_inventaris_bersih": data_bersih
    }
