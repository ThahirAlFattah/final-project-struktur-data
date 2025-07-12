class Transaksi:
    def __init__(self, tanggal, kategori, tipe, jumlah):
        self.tanggal = tanggal
        self.kategori = kategori
        self.tipe = tipe
        self.jumlah = jumlah
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_transaksi(self, tanggal, kategori, tipe, jumlah):
        transaksi_baru = Transaksi(tanggal, kategori, tipe, jumlah)
        if not self.head:
            self.head = transaksi_baru
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = transaksi_baru
