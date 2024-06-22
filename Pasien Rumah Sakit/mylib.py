from tabulate import tabulate

daftarPasien = {
    321: [1, 321, 'Raihan', 'Laki-laki', 'REGULER', 'Jogja', 'Diabetes', 'BPJS'],
    322: [2, 322, 'Lala', 'Perempuan', 'VVIP', 'Semarang', 'Mata Rabun', 'NON BPJS'],
    323: [3, 323, 'Andi', 'Laki-laki', 'VIP', 'Purwokerto', 'Ginjal', 'NON BPJS'],
    324: [4, 324, 'Sekar', 'Perempuan', 'VIP', 'Malang', 'Paru-paru', 'BPJS'],
    325: [5, 325, 'Lintang', 'Perempuan', 'REGULER', 'Surabaya', 'Usus Buntu', 'BPJS']
}

#Fungsi untuk menampilkan database dalam bentuk tabulate
def tampilkan(database, header=['No', 'NIK', 'Nama', 'Jenis Kelamin', 'Jenis Kamar', 'Kota', 'Penyakit', 'Jenis Pembayaran']):
    print(tabulate(database.values(), headers=header, tablefmt='pretty'))

#Fungsi untuk menampilkan menu
def tampilanMenu(database, header=['No', 'Perintah']):
    print(tabulate(database, headers=header, tablefmt='grid'))

#Fungsi untuk memvalidasi input dengan tipe data string
def stringValidation(title):
    while True:
        teks = input(title)
        if teks.isalpha() == True:
            break
        else:
            print('Input Anda Salah. Silahkan inputkan alfabet!')
    return teks.capitalize()

#Fungsi untuk memvalidasi input dengan tipe data integer
def integerValidation(title, minval=0, maxval=999):
    while True:
        num = input(title)
        try:
            num = int(num)
            if num >= minval and num <= maxval:
                break
            else:
                print(f'Silahkan inputkan angka diantara {minval} dan {maxval}')
        except:
            print('Input Anda Salah. Silahkan inputkan angka!')
    return num

#Fungsi untuk input gender sesuai dengan aturan
def inputGender():
    while True:
        gender = stringValidation(title='Masukan Jenis Kelamin Pasien [L/P]: ').lower()
        if gender == 'l':
            return 'Laki-laki'
        elif gender == 'p':
            return 'Perempuan'
        else:
            print(f'Gender {gender} yang anda masukan salah. Silahkan masukan ulang!')
            continue

#Fungsi untuk input jenis kamar sesuai aturan
def inputKamar():
    while True:
        kamar = stringValidation(title='Masukan Jenis Kamar Pasien: ').lower()
        if kamar == 'vvip':
            return 'VVIP'
        elif kamar == 'vip':
            return 'VIP'
        elif kamar == 'reguler':
            return 'REGULER'
        else:
            print(f'Kamar {kamar} Tidak Tersedia. Silahkan Inputkan Sesuai Arahan')
            continue

#Fungsi untuk input jenis pembayaran sesuai aturan
def inputJenisPembayaran():
    while True:
        jenisPembayaran = stringValidation(title='Masukan Jenis Pembayaran Pasien: ').lower()
        if jenisPembayaran == 'bpjs':
            return 'BPJS'
        elif jenisPembayaran == 'nonbpjs':
            return 'NON BPJS'
        else:
            print(f'Jenis Pembayaran {jenisPembayaran} Tidak Tersedia!')
            continue

#Fungsi untuk menampilkan menu pada sub menu 1
def subMenu1():
    while True:
        # Menampilkan menu pada sub menu 1
        listMenu1 = [
            (1, 'Tampilkan Seluruh Data Pada Database'),
            (2, 'Tampilkan Data Tertentu Sesuai NIK'),
            (3, 'Kembali Ke Menu Utama')
        ]
        print('\n\t=== List Menu Pada Sub Menu 1 ===')
        tampilanMenu(database=listMenu1)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        bilMenu1 = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if bilMenu1 == '1':
            print('\t\t\t=========== Data Pasien Dalam Rumah Sakit ===========')
            tampilkan(daftarPasien)
        elif bilMenu1 == '2':
            pasienBerdasarkanNIK(daftarPasien)
        elif bilMenu1 == '3':
            break
        else:
            print('=== Input anda salah. Silahkan input ulang sesuai dengan angka pada Menu! ===')

#Fungsi untuk mencari value berdasarkan NIK nya   
def pasienBerdasarkanNIK(nik):
    #Membuat dictionary kosong untuk memasukan data
    dataNIK = {}

    #Menginput NIK yang ingin dicari
    nik = integerValidation(
        title='Masukan NIK yang ingin dicari: ',
        maxval=999
    )
    for key, val in daftarPasien.items():
        if nik == key:
            #Menyimpan seluruh value data pada variabel baru
            valCopy = val[:]

            #Membuat Kolom No pada index[0] menjadi 1
            valCopy[0] = 1

            #Mengupdate atau menambahkan variabel yg niknya sama ke variabel dataNIK
            dataNIK.update({nik: valCopy})

            #Menampilkan data sesuai dengan NIK yang dimasukan
            print('\n\t\t== Data Pasien Berdasarkan NIK yang Di Cari Pada Rumah Sakit ==')
            tampilkan(database=dataNIK, header=['No', 'NIK', 'Nama', 'Jenis Kelamin', 'Jenis Kamar', 'Kota', 'Penyakit', 'Jenis Pembayaran'])
            break
    #Jika NIK tidak terdapat dalam database
    else:
        print('=== NIK Tidak Ditemukan Dalam Database! ===')

#Fungsi untuk menampilkan menu pada sub menu 2
def subMenu2():
    while True:
        # Menampilkan menu pada sub menu 2
        listMenu2 = [
            (1, 'Memasukan Data Baru ke Database'),
            (2, 'Kembali Ke Menu Utama')
        ]
        print('\n     === List Menu Pada Sub Menu 2 ===')
        tampilanMenu(database=listMenu2)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        bilMenu2 = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if bilMenu2 == '1':
            tambahData(daftarPasien)
        elif bilMenu2 == '2':
            break
        else:
            print('=== Input anda salah. Silahkan input ulang sesuai dengan angka pada Menu! ===')

#Fungsi menambahkan data
def tambahData(nik):
    #Memberikan keterangan untuk inputan
    ketInput = [
        (1, 'Gender', '(L: Laki-laki) dan (P: Perempuan)'),
        (2, 'Kamar', 'VVIP, VIP, REGULER'),
        (3, 'Jenis Pembayaran', 'BPJS dan NON BPJS (Inputkan tanpa spasi -> nonbpjs)')
    ]
    print('\n\t\t== Keterangan Untuk Memasukan Data ke Dalam Database ==')
    tampilanMenu(database=ketInput, header=['No', 'Kolom', 'Keterangan'])

    #Membuat list kosong untuk menampung data baru yang akan di input
    listValue = []

    #Memvalidasi bahwa NIK harus berjumlah 3 digit
    while True:
        #Menginputkan NIK yang ingin ditambahkan dalam data
        nik = integerValidation(title='Masukan NIK yang ingin ditambahkan kedalam Data: ')

        #Memvalasidasi bahwa NIK harus berjumlah 3 digit
        if len(str(nik)) == 3:
            #Mencari nik yang sama di database
            while nik not in daftarPasien.keys():
                #Menentukan kolom No pada tabel
                Nomor = len(daftarPasien) + 1 #Untuk penomoran karena tidak sesuai index jadi panjang data ditambahkan 1
                
                #Menginput nama pasien dan dimasukan ke variabel nama
                nama = input('Masukan Nama Pasien: ').capitalize() 
                
                #Menginput jenis kelamin sesuai dengan aturan yang ada
                gender = inputGender()
                
                #Menginput jenis kamar sesuai dengan aturan yang ada
                kamar = inputKamar()

                #Menginput asal kota
                asalKota = stringValidation(title='Masukan Asal Kota Pasien: ')
                
                #Menginput jenis penyakit pasien
                penyakit = input('Masukan Penyakit Pasien: ').title()
                
                #Menginput jenis pembayaran sesuai dengan aturan yang ada
                jenisPembayaran = inputJenisPembayaran()
                
                #Memasukan input data pasien baru ke list bernama listValue
                listValue = [Nomor, nik, nama, gender, kamar, asalKota, penyakit, jenisPembayaran]
                
                #Melakukan konfirmasi apakah data yang sudah diinput akan disave atau tidak
                while True:
                    konfirmasi = stringValidation('Apakah Anda ingin menyimpan data? [Yes/No]: ').lower()
                    
                    #Data yang sudah di input tidak di save
                    if konfirmasi in ['no', 'n', 'tidak']:
                        print('\n\t\t=== Data Tidak Tersimpan ke Database ===')
                        return
                    
                    #Data yang sudah di input akan di save atau ditambahka ke database
                    elif konfirmasi in ['yes', 'y', 'ya']:
                        daftarPasien.update({nik: listValue})
                        print('=== Data Sudah Tersimpan ke Database ===')
                        print('\n\t\t\t=========== Data Pasien Dalam Rumah Sakit ===========')
                        tampilkan(daftarPasien)
                        break

                    #Jika salah memasukan konfirmasi input
                    else:
                        print("Input Anda Tidak Valid. Silahkan masukkan 'Yes' atau 'No'.")
                        continue
                break
            
            #Jika NIK yang di input sudah ada di dalam database
            else:
                print('NIK Sudah Ada dalam Data! Tidak Dapat Menginput NIK yang sama!')
            break
        else:
            #Jika NIK tidak berjumlah 3 digit
            print('NIK Harus Berjumlah 3 Digit!')

#Fungsi untuk menampilkan menu pada sub menu 3
def subMenu3():
    while True:
        # Menampilkan menu pada sub menu 3
        listMenu3 = [
            (1, 'Mengedit Data di Database'),
            (2, 'Kembali Ke Menu Utama')
        ]
        print('\n  === List Menu Pada Sub Menu 3 ===')
        tampilanMenu(database=listMenu3)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        bilMenu3 = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if bilMenu3 == '1':
            ubahData(daftarPasien)
        elif bilMenu3 == '2':
            break
        else:
            print('===Input anda salah. Silahkan input ulang!===')

#Fungsi untuk mengubah data pada database
def ubahData(nik):
    #Menginput idnik yang ingin diubah
    nik = integerValidation(title='Masukan NIK yang ingin diubah datanya: ')

    #Membuat dict kosong untuk nantinya ditampilkan sementara
    dataSementara = {}

    #Melakukan iterasi key dan value pada database
    for key, val in daftarPasien.items():
        if nik == key:
            #Memasukan data yang NIK nya sama dengan idNik yang dimasukan
            dataSementara.update({nik: daftarPasien[nik]})
            tampilkan(dataSementara)

            while True:
                #Melakukan konfirmasi kepada user
                print('=== JIKA KOLOM TERDAPAT SPASI MAKA INPUTKAN TANPA SPASI ===')
                konfirmasi = stringValidation(title='Apakah anda yakin ingin mengedit data ini? [Yes/No]: ').lower()
                
                #Jika user menginputkan tidak
                if konfirmasi in ['no', 'n', 'tidak']:
                    print('=== Data Tidak Jadi di Edit ===')
                    break

                #Jika user menginputkan iya
                elif konfirmasi in ['yes', 'y', 'ya']:
                    while True:
                        #Memberi pilihan keuser kolom mana yang ingin di edit
                        kolomEdit = stringValidation(title='Masukan kolom yang ingin di edit: ').lower()
                        #Kolom nama
                        if kolomEdit == 'nama':
                            nama = stringValidation(title='Masukan Nama Pasien: ')
                            konfNama = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Nama? [Yes/No]: ').lower()
                            if konfNama in ['yes', 'y', 'ya']:
                                val[2] = nama
                                break
                            elif konfNama in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        #Kolom kamar
                        elif kolomEdit == 'jeniskelamin':
                            jenisKelamin = inputGender()
                            konfJK = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Jenis Kelamin? [Yes/No]: ').lower()
                            if konfJK in ['yes', 'y', 'ya']:
                                val[3] = jenisKelamin
                                break
                            elif konfJK in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        #Kolom jenis kelamin
                        elif kolomEdit == 'jeniskamar':
                            jenisKamar = inputKamar()
                            konfJenisKamar = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Jenis Kamar? [Yes/No]: ').lower()
                            if konfJenisKamar in ['yes', 'y', 'ya']:
                                val[4] = jenisKamar
                                break
                            elif konfJenisKamar in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        elif kolomEdit == 'kota':
                            kota = stringValidation(title='Masukan Kota Pasien: ')
                            konfKota = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Kota? [Yes/No]: ').lower()
                            if konfKota in ['yes', 'y', 'ya']:
                                val[5] = kota
                                break
                            elif konfKota in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        #Kolom penyakit
                        elif kolomEdit == 'penyakit':
                            penyakit = input('Masukan Penyakit Pasien: ').title()
                            konfPenyakit = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Penyakit? [Yes/No]: ').lower()
                            if konfPenyakit in ['yes', 'y', 'ya']:
                                val[6] = penyakit
                                break
                            elif konfPenyakit in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        #Kolom jenis pembayaran
                        elif kolomEdit == 'jenispembayaran':
                            jenisPembayaran = inputJenisPembayaran()
                            konfJP = stringValidation(title='Apakah Anda Yakin Ingin Mengganti Jenis Pembayaran? [Yes/No]: ').lower()
                            if konfJP in ['yes', 'y', 'ya']:
                                val[7] = jenisPembayaran
                                break
                            elif konfJP in ['no', 'n', 'tidak']:
                                break
                            else:
                                print("Input Tidak Valid. Silahkan Masukan 'Yes' atau 'No'.")
                            break
                        #Untuk kolom nik dan no tidak dapat diubah
                        elif kolomEdit == 'nik' or kolomEdit == 'no':
                            print('Kolom No dan NIK tidak dapat di Ubah!')
                            continue
                        #Jika user menginputkannya tidak sesuai dengan pilihan
                        else:
                            print('Input yang anda masukan salah!. Silahkan Input Kembali')
                            continue   
                    #Memberitahu user bahwa data telah diperbaharui
                    print('Data Pada Database Telah Di Pebaharui')
                    break
                #Jika user tidak menginputkan yes atau no pada konfirmasi
                else:
                    print("Input tidak valid. Silahkan masukkan 'Yes' atau 'No'.")
                    continue
            break
    #Jika nik yang di inputkan tidak sesuai dengan yang didata
    else:
        print('NIK yang Anda Cari Tidak Ada di Dalam Data!')

#Fungsi untuk menampilkan menu pada sub menu 4
def subMenu4():
    while True:
        # Menampilkan menu pada sub menu 4
        listMenu4 = [
            (1, 'Menghapus Data dari Database'),
            (2, 'Kembali Ke Menu Utama')
        ]
        print('\n   === List Menu Pada Sub Menu 4 ===')
        tampilanMenu(database=listMenu4)

        # Meminta input nomor sesuai pilihan menu
        print('=============================')
        bilMenu4 = input("Masukkan angka sesuai menu: ")
        print('=============================')

        # Menjalankan fungsi sesuai pilihan menu
        if bilMenu4 == '1':
            hapusData(daftarPasien)
        elif bilMenu4 == '2':
            break
        else:
            print('===Input anda salah. Silahkan input ulang!===')

#Fungsi untuk menghapus data dari database
def hapusData(nik):
    #Menampilkan data agar user mudah dalam mencari nik
    tampilkan(daftarPasien)

    #menginputkan nik yang akan dihapus
    nik = integerValidation(title='Masukan NIK yang ingin dihapus: ')
    
    #Melakukan iterasi untuk data pada database
    for key, val in daftarPasien.items():
        #Jika idnik yang diinputkan sama dengan value pada index [1]
        if nik == val[1]:
            while True:
                #Konfirmasi apakah ingin menghapus data
                konfirmasi = stringValidation('Apakah Anda ingin menghapus data? [Yes/No]: ').lower()

                #Jika user menginputkan tidak maka data tidak akan dihpaus
                if konfirmasi in ['no', 'n', 'tidak']:
                    print('=== Data Gagal di Hapus dari Database ===')
                    return
                
                #Jika user menginputkan iya maka data akan dihapus
                elif konfirmasi in ['yes', 'y', 'ya']:
                    del daftarPasien[key]

                    #Perulangan untuk kolom no karena kolom tidak sesuai dengan index
                    #kolom no akan menyesuaikan
                    for key, val in enumerate(daftarPasien.values()):
                        if key != val[0]:
                            daftarPasien[val[1]][0] = key + 1
                    print('\t\t\t=== Data Berhasil di Hapus dari Database ===')
                    tampilkan(daftarPasien)
                    break 
                
                #jika user menginputkan selain yes atau no pada kolom konfirmasi
                else:
                    print("Input tidak valid. Silahkan masukkan 'Yes' atau 'No'.")
            break
    #Jika nik yang di inputkan tidak ada dalam data
    else:
        print('NIK yang Anda Masukan Tidak Ada dalam Database. Silahkan Inputkan Ulang!')