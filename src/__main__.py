import os
import sys
import csv
import mylib

#Membersihkan terminal ketika dijalankan
def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

#Menginisialisasikan data yang beruoa file csv
def initialize_db():
    """
    A function to initialize the database 

    Returns:
        dict: Fruit database
    """
    with open(PATH, 'r', newline='') as file:
        # Membuat objek reader
        reader = csv.reader(file, delimiter=",")
        # Inisialisasi database kosong
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            no, nik, nama, umur, jenisKelamin, jenisKamar, asalKota, penyakit, jenisPembayaran = row
            database.update({int(nik): [int(no), int(nik), nama, int(umur), jenisKelamin, jenisKamar, asalKota, penyakit, jenisPembayaran]})
    
    return database


def main():
    global database
    listMenu = [
        (1, 'Report Data Pasien'),
        (2, 'Menambah Data Pasien'),
        (3, 'Mengubah Data Pasien'),
        (4, 'Menghapus Data Pasien'),
        (5, 'Exit')
    ]

    while True:
        # Menampilkan tampilan utama
        print('=== Menu Untuk Menjalankan Program ===')
        mylib.tampilanMenu(listMenu)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        option = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if option == '1':
            mylib.subMenu1(database)
        elif option == '2':
            mylib.subMenu2(database)
        elif option == '3':
            mylib.subMenu3(database)
        elif option == '4':
            mylib.subMenu4(database)
        elif option == '5':
            break
        else:
            print('Input anda salah. Silahkan input ulang!')

        # Menjaga agar database selalu diperbarui
        with open(PATH, 'w', newline='') as file:
            # Membuat objek writer
            writer = csv.writer(file, delimiter=",")
            database = mylib.urutNIK(database)
            # Menulis data ke dalam file csv
            writer.writerows(database.values())

if __name__ == "__main__":
    # Membersihkan tampilan user
    clear_screen()
    
     # Mengatur letak file database
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'Data/daftarpasien.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'Data/daftarpasien.csv') 

    # Inisialisasi database
    database = initialize_db()

    # Menjalankan menu utama
    main()