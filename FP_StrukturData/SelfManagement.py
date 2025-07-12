import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

CSV_FILE = "transaksi.csv"

def baca_transaksi():
    try:
        with open(CSV_FILE, mode='r') as file:
            return list(csv.reader(file))
    except FileNotFoundError:
        return []

def simpan_ulang_transaksi(data):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def tambah_transaksi():
    tanggal = entry_tanggal.get()
    kategori = entry_kategori.get()
    tipe = combo_tipe.get()
    jumlah = entry_jumlah.get()

    if not tanggal or not kategori or not tipe or not jumlah:
        messagebox.showwarning("Peringatan", "Semua field harus diisi.")
        return

    try:
        datetime.strptime(tanggal, "%Y-%m-%d")
        jumlah = int(jumlah)
    except ValueError:
        messagebox.showerror("Error", "Tanggal atau jumlah tidak valid.")
        return

    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, kategori, tipe, jumlah])

    tampilkan_transaksi()
    clear_form()
    messagebox.showinfo("Sukses", "Transaksi berhasil ditambahkan.")

def hapus_transaksi():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Pilih data", "Pilih transaksi yang ingin dihapus.")
        return
    index = tree.index(selected[0])
    data = baca_transaksi()
    data.pop(index)
    simpan_ulang_transaksi(data)
    tampilkan_transaksi()

def edit_transaksi():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Pilih data", "Pilih transaksi yang ingin diedit.")
        return
    index = tree.index(selected[0])
    data = baca_transaksi()
    try:
        tanggal = entry_tanggal.get()
        kategori = entry_kategori.get()
        tipe = combo_tipe.get()
        jumlah = int(entry_jumlah.get())
        datetime.strptime(tanggal, "%Y-%m-%d")
    except:
        messagebox.showerror("Error", "Input tidak valid.")
        return
    data[index] = [tanggal, kategori, tipe, str(jumlah)]
    simpan_ulang_transaksi(data)
    tampilkan_transaksi()
    clear_form()
    messagebox.showinfo("Sukses", "Transaksi berhasil diedit.")

def tampilkan_transaksi():
    for row in tree.get_children():
        tree.delete(row)
    data = baca_transaksi()
    for row in data:
        tree.insert("", "end", values=row)

def isi_form(event):
    selected = tree.selection()
    if selected:
        values = tree.item(selected[0], 'values')
        entry_tanggal.delete(0, tk.END)
        entry_kategori.delete(0, tk.END)
        combo_tipe.set("")
        entry_jumlah.delete(0, tk.END)

        entry_tanggal.insert(0, values[0])
        entry_kategori.insert(0, values[1])
        combo_tipe.set(values[2])
        entry_jumlah.insert(0, values[3])

def clear_form():
    entry_tanggal.delete(0, tk.END)
    entry_kategori.delete(0, tk.END)
    combo_tipe.set("")
    entry_jumlah.delete(0, tk.END)

# UI Setup
root = tk.Tk()
root.title("KeuPribadi GUI - CRUD")

# Form Input
frame_form = tk.Frame(root, padx=10, pady=10)
frame_form.pack(fill="x")

tk.Label(frame_form, text="Tanggal (YYYY-MM-DD)").grid(row=0, column=0)
entry_tanggal = tk.Entry(frame_form)
entry_tanggal.grid(row=0, column=1)

tk.Label(frame_form, text="Kategori").grid(row=1, column=0)
entry_kategori = tk.Entry(frame_form)
entry_kategori.grid(row=1, column=1)

tk.Label(frame_form, text="Tipe").grid(row=2, column=0)
combo_tipe = ttk.Combobox(frame_form, values=["pemasukan", "pengeluaran"])
combo_tipe.grid(row=2, column=1)

tk.Label(frame_form, text="Jumlah").grid(row=3, column=0)
entry_jumlah = tk.Entry(frame_form)
entry_jumlah.grid(row=3, column=1)

btn_frame = tk.Frame(frame_form)
btn_frame.grid(row=4, columnspan=2, pady=10)

tk.Button(btn_frame, text="Tambah", command=tambah_transaksi, width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Edit", command=edit_transaksi, width=10).pack(side="left", padx=5)
tk.Button(btn_frame, text="Hapus", command=hapus_transaksi, width=10).pack(side="left", padx=5)

# Table View
frame_table = tk.Frame(root, padx=10, pady=10)
frame_table.pack(fill="both", expand=True)

tree = ttk.Treeview(frame_table, columns=("Tanggal", "Kategori", "Tipe", "Jumlah"), show="headings")
tree.heading("Tanggal", text="Tanggal")
tree.heading("Kategori", text="Kategori")
tree.heading("Tipe", text="Tipe")
tree.heading("Jumlah", text="Jumlah")
tree.bind("<<TreeviewSelect>>", isi_form)
tree.pack(fill="both", expand=True)

tampilkan_transaksi()
root.mainloop()