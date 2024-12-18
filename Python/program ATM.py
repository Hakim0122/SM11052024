from datetime import datetime

# Daftar akun ATM
# Format: [username, pin, saldo, nomor rekening, jumlah nomor rekening, nama bank]
daftar_akun = [
    ['Candra', 12345, 1100000, 1112229991, 10, 'BCA'],
    ['Hakim', 23456, 1500000, 1113339992, 10, 'BCA'],
    ['Novi', 34567, 1400000, 1114449993, 10, 'BCA'],
    ['Sasa', 45678, 1600000, 1115559994, 10, 'BCA']
]

kode_bank = [
    ['BRI', '002', 15],
    ['CIMB Niaga', '451', 13],
    ['Mandiri', '008', 13],
    ['BTN', '200', 16]
]

kode_ewallet = [
    ['Shopee', 122],
    ['Dana', 3901],
    ['Gopay', 70001],
    ['Ovo', 39358]
]

def cek_akun(username, pin):
    for akun in daftar_akun:
        if akun[0] == username and akun[1] == pin:
            return akun

def ini_nama_bank(kode):
    for bank in kode_bank:
        if bank[1] == kode:
            return bank

def va_wallet(va):
    for ewallet in kode_ewallet:
        if ewallet[1] == va:
            return ewallet

def tampilan_menu():
    print("=======================")
    print("-Selamat Datang di ATM-")
    print("=======================")
    print("1. Cek Saldo")
    print("2. Transfer")
    print("3. Top Up E-Wallet")
    print("4. Tarik Tunai")
    print("5. Setor Tunai")
    print("6. Keluar")
    print("=======================")

def cek_saldo(akun):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("Info: ")
    print(waktu)
    print("Rekening", akun[3])
    print("Saldo anda saat ini: ")
    print("Rp.", akun[2])
    print("~~~~~~~~~~~~~~~~~~~~~~~")

def transfer(akun):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=======================")
    print("1. Antar rekening")
    print("2. Antar bank")
    print("3. Batal")
    print("=======================")
    pilih = int(input("Pilih 1/2/3: "))
    if pilih == 1:
        while True:
            print("-----------------------")
            nomor_rekening = input("Masukan nomor rekening: ")
            if len(nomor_rekening) == akun[4]:
                nomor_rekening = int(nomor_rekening)
                print("-----------------------")
                jumlah_transfer = int(input("Masukan nominal: "))
                print("-----------------------")
                while True:
                    pin = int(input("Masukan pin anda: "))
                    if pin == akun[1]:
                        if jumlah_transfer <= akun[2]:
                            akun[2] -= jumlah_transfer
                            print("~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Transfer berhasil")
                            print(waktu)
                            print("Nomor rekening", nomor_rekening)
                            print("Nominal Rp.", jumlah_transfer)
                            print("~~~~~~~~~~~~~~~~~~~~~~~")
                            return
                        else:
                            print("~~~~~~~~~~~~~~~~~~~~~~~")
                            print("Saldo tidak mencukupi")
                            print("~~~~~~~~~~~~~~~~~~~~~~~")
                            exit()
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Pin salah!")
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("Nomor rekening harus", akun[4], "digit")
                print("~~~~~~~~~~~~~~~~~~~~~~~")
    elif pilih == 2:
        while True:
            print("-----------------------")
            kode = input("Masukan kode bank: ")
            bank = ini_nama_bank(kode)
            biaya = 6500
            if bank:
                nama_bank, kode_bank, panjang_rekening = bank
                print("Bank: ", nama_bank)
                print("-----------------------")
                while True:
                    nomor_rekening = input("Masukan nomor rekening: ")
                    print("-----------------------")
                    if len(nomor_rekening) == panjang_rekening:
                        nomor_rekening = int(nomor_rekening)
                        jumlah_transfer = int(input("Masukan nominal: "))
                        print("-----------------------")
                        while True:
                            pin = int(input("Masukan pin anda: "))
                            if pin == akun[1]:
                                if jumlah_transfer <= akun[2]:
                                    akun[2] -= (jumlah_transfer + biaya)
                                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Transfer berhasil")
                                    print(waktu)
                                    print("Ke", nama_bank)
                                    print("Nomor rekening", nomor_rekening)
                                    print("Nominal Rp.", jumlah_transfer)
                                    print("Biaya Rp. ", biaya)
                                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                                    return
                                else:
                                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Saldo tidak mencukupi")
                                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                                    break
                            else:
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Pin salah!")
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Nomor rekening harus", panjang_rekening, "digit")
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("Kode bank salah")
                print("~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        return
    
def top_up(akun):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        print("-----------------------")
        kode_va = int(input("Masukan kode e-wallet: "))
        ewallet = va_wallet(kode_va)
        if ewallet:
            nama_ewallet, kode_va = ewallet
            print("Top Up", nama_ewallet)
            nomor_hp = input("Masukan Nomer HP: ")
            if 11 <= len(nomor_hp) <= 13:
                jumlah_topup = int(input("Masukan nominal: "))
                while True:
                    pin = int(input("Masukan pin: "))
                    if pin == akun[1]:
                        if jumlah_topup <=49000:
                            biaya_admin = 500
                            if jumlah_topup <= akun[2]:
                                akun[2] -= (jumlah_topup + biaya_admin)
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Top Up berhasil")
                                print(waktu)
                                print("E-Wallet", nama_ewallet)
                                print("Nominal Rp.", jumlah_topup)
                                print("Biaya Rp", biaya_admin)
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                return
                            else:
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Saldo tidak mencukupi")
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                break
                        else:
                            if jumlah_topup <= akun[2]:
                                akun[2] -= jumlah_topup
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Top Up berhasil")
                                print(waktu)
                                print("E-Wallet", nama_ewallet)
                                print("Nominal Rp.", jumlah_topup)
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                return
                            else:
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                print("Saldo tidak mencukupi")
                                print("~~~~~~~~~~~~~~~~~~~~~~~")
                                break
                    else:
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Pin yang anda masukkan salah.")
                        print("~~~~~~~~~~~~~~~~~~~~~~~")
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("Nomor HP salah")
                print("~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("Kode e-wallet salah")
            print("~~~~~~~~~~~~~~~~~~~~~~~")

def tarik_tunai(akun):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        print("-----------------------")
        jumlah_tarik = int(input("Masukan nominal: "))
        if jumlah_tarik % 50000 == 0:
            while True:
                pin = int(input("Masukan pin anda: "))
                if pin == akun[1]:
                    if jumlah_tarik <= akun[2]:
                       akun[2] -= jumlah_tarik
                       print("~~~~~~~~~~~~~~~~~~~~~~~")
                       print("Berhasil")
                       print(waktu)
                       print("Tarik tunai Rp.", jumlah_tarik)
                       print("~~~~~~~~~~~~~~~~~~~~~~~")
                       return
                    else:
                       print("~~~~~~~~~~~~~~~~~~~~~~~")
                       print("Jumlah saldo anda tidak mencukupi")
                       print("~~~~~~~~~~~~~~~~~~~~~~~")
                       break
                else:
                   print("~~~~~~~~~~~~~~~~~~~~~~~")
                   print("Pin yang anda masukkan salah.")
                   print("~~~~~~~~~~~~~~~~~~~~~~~")
        else:
           print("~~~~~~~~~~~~~~~~~~~~~~~")
           print("Maaf, penarikan tunai")
           print("Hanya bisa dilakukan")
           print("Dengan pecahan 50000/100000")
           print("~~~~~~~~~~~~~~~~~~~~~~~")

def setor_tunai(akun):
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        print("-----------------------")
        jumlah_setor = int(input("Masukan uang anda: "))
        if jumlah_setor % 50000 == 0:
            while True:
                pin = int(input("Masukan pin anda: "))
                if pin == akun[1]:
                    akun[2] += jumlah_setor
                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Berhasil")
                    print(waktu)
                    print("Saldo Rp.", jumlah_setor)
                    print("Telah ditambahkan")
                    print("Ke rekening anda")
                    cek_saldo(akun)
                    return
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                    print("Pin yang anda masukkan salah")
                    print("~~~~~~~~~~~~~~~~~~~~~~~")
                    break
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~")
            print("Maaf, setor tunai")
            print("Hanya bisa dilakukan")
            print("Dengan pecahan 50000/100000")
            print("~~~~~~~~~~~~~~~~~~~~~~~")

while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("----SELAMAT DATANG----")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    username = input("Masukan Username: ")
    pin = int(input("Masukan Pin Anda: "))
    print("~~~~~~~~~~~~~~~~~~~~~~~")

    akun = cek_akun(username, pin)

    if akun:
        while True:
            tampilan_menu()
            pilihan = int(input("Pilih 1/2/3/4/5/6: "))
            if pilihan == 1:
                cek_saldo(akun)
            elif pilihan == 2:
                transfer(akun)
            elif pilihan == 3:
                top_up(akun)
            elif pilihan == 4:
                tarik_tunai(akun)
            elif pilihan == 5:
                setor_tunai(akun)
            elif pilihan == 6:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("Terimakasih Telah")
                print("Menggunakan Layanan ATM")
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                exit()
            else:
                print("~~~~~~~~~~~~~~~~~~~~~~~")
                print("Pilihan tidak valid")
                print("~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("Username atau pin salah")
