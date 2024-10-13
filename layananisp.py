# Simulasi Database Pengguna
database = {
    "081234567890": {"saldo": 50000},
    "089876543210": {"saldo": 10000}
}

def cek_saldo(nomor):
    return database.get(nomor, {}).get("saldo", 0)

def transfer_pulsa(pengirim, penerima, jumlah):
    if pengirim not in database or penerima not in database:
        return "Nomor tidak valid."
    
    if jumlah <= 0:
        return "Jumlah tidak valid."
    
    saldo_pengirim = cek_saldo(pengirim)
    if saldo_pengirim < jumlah:
        return "Saldo tidak cukup."

    database[pengirim]["saldo"] -= jumlah
    database[penerima]["saldo"] += jumlah
    return f"Transfer {jumlah} berhasil ke {penerima}."

def main_menu():
    print("Menu USSD *858#")
    print("1. Cek Saldo")
    print("2. Transfer Pulsa")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        nomor = input("Masukkan nomor Anda: ")
        saldo = cek_saldo(nomor)
        print(f"Saldo Anda: {saldo}")
    elif pilihan == "2":
        pengirim = input("Masukkan nomor Anda: ")
        penerima = input("Masukkan nomor penerima: ")
        jumlah = int(input("Masukkan jumlah pulsa: "))
        hasil = transfer_pulsa(pengirim, penerima, jumlah)
        print(hasil)
    elif pilihan == "0":
        print("Terima kasih telah menggunakan layanan ini.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    while True:
        main_menu()
        lanjut = input("Lanjutkan? (y/n): ").lower()
        if lanjut != 'y':
            break
