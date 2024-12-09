# Praktikum_pertemuan_11

*A. ALGORITMA PROGRAM*

1. Mulai

   Program dimulai.

2. Tampilkan Menu Utama

   Menampilkan menu pilihan untuk pengguna:

   >Tambah Mahasiswa

   >Tampilkan Mahasiswa

   >Hapus Mahasiswa

   >Ubah Data Mahasiswa

   >Keluar

3. Pengguna Memilih Menu

   Jika Pilihan = 1 (Tambah Mahasiswa):

   >Input nama, NIM, dan nilai.

   >Validasi nama (minimal 3 karakter) dan nilai (antara 0 dan 100).

   >Jika nama sudah ada, tampilkan pesan kesalahan.

   >Tentukan status berdasarkan nilai.

   >Tambahkan mahasiswa ke dalam daftar.

   >Kembali ke Menu Utama.

   Jika Pilihan = 2 (Tampilkan Mahasiswa):

   >Tampilkan daftar mahasiswa yang ada.
   
   >Kembali ke Menu Utama.

   Jika Pilihan = 3 (Hapus Mahasiswa):

   >Input nama mahasiswa yang ingin dihapus.

   >Cek apakah mahasiswa ada dalam daftar.

   >Jika ada, hapus mahasiswa.

   >Kembali ke Menu Utama.

   Jika Pilihan = 4 (Ubah Data Mahasiswa):

   >Input nama mahasiswa yang ingin diubah.

   >Tampilkan pilihan untuk mengubah NIM atau nilai.

   >Jika memilih untuk mengubah nilai, lakukan validasi dan perbarui nilai.

   >Tentukan status baru berdasarkan nilai yang diubah.

   >Kembali ke Menu Utama.

   Jika Pilihan = 5 (Keluar):

   >Program berhenti dan tampilkan pesan terima kasih.

4. Kembali ke Menu Utama

   Jika pengguna memilih menu selain keluar, program kembali menampilkan menu utama untuk memilih tindakan selanjutnya.

#

*B. CODE PROGRAM DAN PENJELASAN*

![image](https://github.com/user-attachments/assets/b2081305-63cd-4adf-b699-e77ed0035f46)

![image](https://github.com/user-attachments/assets/9109f7b6-2379-4efd-9e44-71e42e39bc09)

PENJELASAN :

![image](https://github.com/user-attachments/assets/0ff6dbdc-17e6-4f01-9882-80d7aebdf0a9)

__init__(self) adalah metode yang dijalankan otomatis ketika kita membuat objek dari kelas SistemMahasiswa. Di dalam metode ini, kita membuat atribut __daftar_mahasiswa yang berupa dictionary kosong. Dictionary ini akan digunakan untuk menyimpan data mahasiswa, di mana nama mahasiswa menjadi kunci (key), dan informasi seperti NIM, nilai, dan status menjadi nilai (value).


