import mylib

def main():
    listMenu = [
        (1, 'Report Data Pasien'),
        (2, 'Menambah Data Pasien'),
        (3, 'Mengubah Data Pasien'),
        (4, 'Menghapus Data Pasien'),
        (5, 'Exit')
    ]

    while True:
        # Menampilkan tampilan utama
        mylib.tampilanMenu(listMenu)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        option = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if option == '1':
            mylib.subMenu1()
        elif option == '2':
            mylib.subMenu2()
        elif option == '3':
            mylib.subMenu3()
        elif option == '4':
            mylib.subMenu4()
        elif option == '5':
            break
        else:
            print('Input anda salah. Silahkan input ulang!')

# Menjalankan program utama
main()
#Tes