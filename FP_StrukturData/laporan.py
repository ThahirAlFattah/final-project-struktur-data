def laporan_per_kategori(data_csv):
    laporan = {}
    for row in data_csv:
        kategori = row[1]
        tipe = row[2]
        jumlah = int(row[3])

        if kategori not in laporan:
            laporan[kategori] = {"pemasukan": 0, "pengeluaran": 0}

        laporan[kategori][tipe] += jumlah

    return laporan

def tampilkan_laporan(laporan):
    print("\n📊 Laporan Keuangan Berdasarkan Kategori:")
    for kategori, data in laporan.items():
        print(f"- {kategori}: +Rp{data['pemasukan']} / -Rp{data['pengeluaran']}")
