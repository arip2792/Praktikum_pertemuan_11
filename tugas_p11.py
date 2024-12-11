print("================================== ARIEF ADJI ==================================")

# Daftar nilai mahasiswa

daftar_nilai = []

def tambah(nama, nim, kelas, nilai):
    daftar_nilai.append({"nama": nama, "nim": nim, "kelas": kelas, "nilai": nilai})
    print(f"Data untuk {nama} berhasil ditambahkan.")

def tampilkan():
    if not daftar_nilai:
        print("Tidak ada data mahasiswa.")
        return
    print("\nDaftar Nilai Mahasiswa:")
    print("+--------------------+------------+--------+------------+")
    print("|         Nama       |    NIM     |  Kelas |    Nilai   |")
    print("+--------------------+------------+--------+------------+")
    for data in daftar_nilai:
        print("| {:<18} | {:<10} | {:<6} | {:<10} |".format(data['nama'], data['nim'], data['kelas'], data['nilai']))
    print("+--------------------+------------+--------+------------+")

def hapus(nama):
    global daftar_nilai
    for data in daftar_nilai:
        if data['nama'] == nama:
            daftar_nilai.remove(data)
            print(f"Data untuk {nama} berhasil dihapus.")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

def ubah(nama, nim_baru, kelas_baru, nilai_baru):
    for data in daftar_nilai:
        if data['nama'] == nama:
            data['nim'] = nim_baru
            data['kelas'] = kelas_baru
            data['nilai'] = nilai_baru
            print(f"Data {nama} berhasil diubah.")
            return
    print(f"Data mahasiswa dengan nama {nama} tidak ditemukan.")

while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih opsi (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        kelas = input("Masukkan kelas mahasiswa: ")
        nilai = float(input("Masukkan nilai mahasiswa: "))
        tambah(nama, nim, kelas, nilai)

    elif pilihan == "2":
        tampilkan()

    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus(nama)

    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        nim_baru = input("Masukkan NIM baru: ")
        kelas_baru = input("Masukkan kelas baru: ")
        nilai_baru = float(input("Masukkan nilai baru: "))
        ubah(nama, nim_baru, kelas_baru, nilai_baru)

    elif pilihan == "5":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
