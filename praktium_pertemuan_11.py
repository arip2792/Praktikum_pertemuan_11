print("==================== ARIEF ADJI ====================")

class SistemMahasiswa:
    def __init__(self):
        self.__daftar_mahasiswa = {}
    
    def tambah(self, nama, nim, nilai):
        if not nama or len(nama) < 3:
            print("Nama harus memiliki minimal 3 karakter!")
            return
        
        if nama.lower() in self.__daftar_mahasiswa:
            print(f"Mahasiswa {nama} sudah ada!")
            return
        
        if nilai >= 85:
            status = "Cumlaude"
        elif nilai >= 75:
            status = "Sangat Baik"
        elif nilai >= 60:
            status = "Baik"
        else:
            status = "Perlu Perbaikan"
        
        self.__daftar_mahasiswa[nama.lower()] = {
            'nim': nim,
            'nilai': nilai,
            'status': status
        }
        print(f"Mahasiswa {nama} berhasil ditambahkan!")
    
    def tampilkan(self):
        if not self.__daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        
        print("\nDaftar Mahasiswa:")
        print("-" * 50)
        print(f"{'Nama':<15} {'NIM':<15} {'Nilai':<10} {'Status'}")
        print("-" * 50)
        
        for nama, data in self.__daftar_mahasiswa.items():
            print(f"{nama.title():<15} {data['nim']:<15} {data['nilai']:<10.2f} {data['status']}")
    
    def hapus(self, nama):
        nama = nama.lower()
        if nama in self.__daftar_mahasiswa:
            del self.__daftar_mahasiswa[nama]
            print(f"Mahasiswa {nama} berhasil dihapus!")
        else:
            print(f"Mahasiswa {nama} tidak ditemukan!")
    
    def ubah(self, nama):
        nama = nama.lower()
        if nama not in self.__daftar_mahasiswa:
            print(f"Mahasiswa {nama} tidak ditemukan!")
            return
        
        print(f"\nUbah Data Mahasiswa: {nama.title()}")
        
        print("Pilih data yang ingin diubah:")
        print("1. NIM")
        print("2. Nilai")
        
        pilihan = input("Masukkan pilihan (1/2): ")
        
        if pilihan == '1':
            nim_baru = input("Masukkan NIM baru: ")
            self.__daftar_mahasiswa[nama]['nim'] = nim_baru
            print("NIM berhasil diperbarui!")
        
        elif pilihan == '2':
            while True:
                try:
                    nilai_baru = float(input("Masukkan nilai baru: "))
                    if 0 <= nilai_baru <= 100:
                        self.__daftar_mahasiswa[nama]['nilai'] = nilai_baru
                        
                        if nilai_baru >= 85:
                            status = "Cumlaude"
                        elif nilai_baru >= 75:
                            status = "Sangat Baik"
                        elif nilai_baru >= 60:
                            status = "Baik"
                        else:
                            status = "Perlu Perbaikan"
                        
                        self.__daftar_mahasiswa[nama]['status'] = status
                        print("Nilai berhasil diperbarui!")
                        break
                    else:
                        print("Nilai harus antara 0-100!")
                except ValueError:
                    print("Input tidak valid!")
        else:
            print("Pilihan tidak valid!")

def main():
    sistem = SistemMahasiswa()
    
    while True:
        print("\nSistem Manajemen Mahasiswa")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Hapus Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM: ")
            try:
                nilai = float(input("Masukkan nilai: "))
                sistem.tambah(nama, nim, nilai)
            except ValueError:
                print("Nilai harus berupa angka!")
        
        elif pilihan == '2':
            sistem.tampilkan()
        
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
            sistem.hapus(nama)
        
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang akan diubah: ")
            sistem.ubah(nama)
        
        elif pilihan == '5':
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
