import random
import datetime
from costumer import Costumer


# DONA HASRUL
print(r"""        ______                    ,__  __                   
        |  _  \____ ,_  __,  ___, | |__| |____,  ____ ._,_ ,_ ,_ ,_
        | | | / _  \| "__ |/ _' | | ,__, |  _  \/ ,__\|  _\| || || |
        | |/ / (_) || | | | ( ) | | |  | | (_) ||__,  | |  | || || |__
        |___/ \____/|_| |_|\__,_| |_|  | |\__,_//____/|_|  \___,/|____\ """)

# LOGO ATM
print("\n")
print("    =   =  =  =   =  =     ===  ===== =   =        ")
print("    == ==     ==  =       =   =   =   == ==        ")
print("    = = =  =  = = =  =    =====   =   = = =        ")
print("    =   =  =  =  ==  =    =   =   =   =   =        ")
print("    =   =  =  =   =  =    =   =   =   =   =        ") 
print("\n")


atm = Costumer(id)

while True:
    id = int(input('Masukkan Pin anda: '))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input('Pin anda salah. Silakan Masukkan Lagi: '))
        trial += 1
    
        if trial == 3:
            print("Error, Silakan Ambil Kartu dan Coba Lagi..")
            exit()

    while True:
        print("Selamat Datang di ATM Progate")
        print("\t1 - Cek Saldo \n\t2 - Debet \n\t3 - Simpan \n\t4 - Ganti Pin \n\t5 - Keluar")
        selectmenu = int(input('Silakan Pilih Menu : '))

        # menu 1 - cek saldo
        if selectmenu == 1:
            print("Saldo Sekarang adalah " + str(atm.checkBalance()) + '\n')

        # menu 2 - debet
        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo :"))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n " + str(nominal) + " ")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance())+ " ")
            else:
                break

            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + " ")
            else:
                print("Maaf Saldo anda tidak cukup melakukan debet!")
                print("Silakan lakukan penambahan Saldo")

        # Menu 3 - Simpan
        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")

            if verify_withdraw == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adala: Rp. " + str(atm.checkBalance()) + " ")
            else:
                break

        # Menu 4 - Ganti pin
        elif selectmenu == 4:
            verify_withdraw = int(input("masukkan pin anda: "))

            while verify_withdraw != atm.checkPin():
                print("pin anda salah, silakan masukkan pin: ")

            update_pin = int(input("Silakan masukkan pin baru: "))
            print("pin anda berhasil di ganti")

            verify_newpin = int(input("Masukkan pin baru: "))

            if verify_newpin == update_pin:
                print("pin baru anda sukses!")
            else:
                print('Maaf pin anda salah!')

        # Menu 5 - Ganti pin
        elif selectmenu == 5:
            noRekord = str(random.randint(100000, 1000000))
            date = str(datetime.datetime.now())
            saldo = str(atm.checkBalance())

            def history():
                file = open("data.txt",'a')
                file.write("\n")
                file.write("No. Rekord : " + noRekord)
                file.write("\nTanggal : " + date)
                file.write("\nSaldo akhir : " + saldo)
                file.write("\n" + 50 * "=")
                file.close

            def struk():
                print(50 * "="+"=======")
                print("| Resi tercetak otomatis saat anda keluar.\t\t| \n| Harap simpan tanda terima ini,\t\t\t| \n| sebagai bukti transaksi anda.\t\t\t\t|")
                print("| No. Rekord : " + noRekord + "\t\t\t\t\t|")
                print("| Tanggal : " + date + "\t\t\t|")
                print("| Saldo akhir : " + saldo + "\t\t\t\t\t|")
                print("| Terima Kasih Telah Menggunakan ATM Progate" + "\t\t|")
                print(50 * "="+"=======")
                exit()

            history()
            print(struk())
        else:
            print("ERROR, Maaf Menu tidak tersedia!")