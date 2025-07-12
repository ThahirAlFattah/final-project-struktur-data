def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus angka!")

def input_tanggal():
    from datetime import datetime
    while True:
        tanggal = input("Tanggal (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal, "%Y-%m-%d")
            return tanggal
        except ValueError:
            print("Format tanggal salah!")
