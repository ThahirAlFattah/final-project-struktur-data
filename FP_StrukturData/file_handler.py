import csv

CSV_FILE = "transaksi.csv"

def simpan_ke_csv(transaksi):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([transaksi.tanggal, transaksi.kategori, transaksi.tipe, transaksi.jumlah])

def baca_semua_transaksi():
    data = []
    try:
        with open(CSV_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    data.append(row)
    except FileNotFoundError:
        open(CSV_FILE, 'w').close()  # Buat file kalau belum ada
    return data

def simpan_ulang_csv(data):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
