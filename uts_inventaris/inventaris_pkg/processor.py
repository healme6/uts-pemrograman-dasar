def bersihkan_dan_validasi(data_mentah):
    """Menghapus duplikat kode barang dan memvalidasi nilai numerik stok serta harga."""
    data_bersih = []
    kode_tercatat = set()
    jumlah_rusak = 0

    for item in data_mentah:
        kode = item.get("kode_barang", "").strip().upper()
        nama = item.get("nama_barang", "").strip()
        kategori = item.get("kategori", "").strip()

        if not kode or not nama or not kategori:
            jumlah_rusak += 1
            continue

        if kode in kode_tercatat:
            jumlah_rusak += 1
            continue

        try:
            stok = int(item.get("stok", 0))
            harga = float(item.get("harga_satuan", 0))
            if stok < 0 or harga < 0:
                jumlah_rusak += 1
                continue
        except (ValueError, TypeError):
            jumlah_rusak += 1
            continue

        kode_tercatat.add(kode)
        data_bersih.append({
            "kode_barang": kode,
            "nama_barang": nama,
            "kategori": kategori,
            "stok": stok,
            "harga_satuan": harga,
            "total_nilai": stok * harga
        })

    return data_bersih, jumlah_rusak


def filter_stok_menipis(data_bersih, batas=5):
    """Menyaring barang dengan stok kurang dari atau sama dengan batas menggunakan list comprehension."""
    return [barang for barang in data_bersih if barang["stok"] <= batas]


def cari_barang(data_bersih, kata_kunci):
    """Mencari barang berdasarkan potongan nama barang secara case-insensitive."""
    kunci = kata_kunci.strip().lower()
    return [barang for barang in data_bersih if kunci in barang["nama_barang"].lower()]


def hitung_rekap_kategori(data_bersih):
    """Menghitung total nilai aset per kategori menggunakan set dan dictionary comprehension."""
    kategori_unik = {barang["kategori"] for barang in data_bersih}
    rekap = {
        kat: sum(b["total_nilai"] for b in data_bersih if b["kategori"] == kat)
        for kat in kategori_unik
    }
    return rekap
