from transaksi import LinkedList
from file_handler import simpan_ke_csv, baca_semua_transaksi, simpan_ulang_csv
from laporan import laporan_per_kategori, tampilkan_laporan
from utils import input_angka, input_tanggal

def tampilkan_daftar(data):
    for i, row in enumerate(data):
        print(f"{i+1}. {row[0]} | {row[1]} | {row[2]} | Rp{row[3]}")

def edit_transaksi():
    data = baca_semua_transaksi()
    if not data:
        print("Belum ada transaksi.")
        return
    tampilkan_daftar(data)
    index = input_angka("Pilih nomor transaksi yang mau diedit: ") - 1
    if 0 <= index < len(data):
        print("Masukkan data baru:")
        data[index][0] = input_tanggal()
        data[index][1] = input("Kategori: ")
        data[index][2] = input("Tipe (pemasukan/pengeluaran): ").lower()
        data[index][3] = str(input_angka("Jumlah (Rp): "))
        simpan_ulang_csv(data)
        print("✅ Transaksi berhasil diedit.")
    else:
        print("❌ Nomor tidak valid.")

def hapus_transaksi():
    data = baca_semua_transaksi()
    if not data:
        print("Belum ada transaksi.")
        return
    tampilkan_daftar(data)
    index = input_angka("Pilih nomor transaksi yang mau dihapus: ") - 1
    if 0 <= index < len(data):
        data.pop(index)
        simpan_ulang_csv(data)
        print("✅ Transaksi berhasil dihapus.")
    else:
        print("❌ Nomor tidak valid.")

def main():
    print("=== Aplikasi KeuPribadi ===")
    riwayat = LinkedList()

    while True:
        print("\nMenu:")
        print("1. Tambah Transaksi")
        print("2. Lihat Riwayat Transaksi")
        print("3. Laporan Keuangan")
        print("4. Edit Transaksi")
        print("5. Hapus Transaksi")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            tanggal = input_tanggal()
            kategori = input("Kategori: ")
            tipe = input("Tipe (pemasukan/pengeluaran): ").lower()
            jumlah = input_angka("Jumlah (Rp): ")

            riwayat.tambah_transaksi(tanggal, kategori, tipe, jumlah)
            simpan_ke_csv(riwayat.head)
            print("✅ Transaksi berhasil ditambahkan.")

        elif pilihan == "2":
            print("\n📄 Riwayat Transaksi:")
            data = baca_semua_transaksi()
            tampilkan_daftar(data)

        elif pilihan == "3":
            data = baca_semua_transaksi()
            laporan = laporan_per_kategori(data)
            tampilkan_laporan(laporan)

        elif pilihan == "4":
            edit_transaksi()

        elif pilihan == "5":
            hapus_transaksi()

        elif pilihan == "6":
            print("Keluar dari aplikasi. 👋")
            break

        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()
