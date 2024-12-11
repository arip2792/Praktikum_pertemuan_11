# Praktikum_pertemuan_11

#

*A. ALGORITMA PROGRAM*


1. Inisialisasi:

   Buat daftar kosong untuk menampung data mahasiswa, misalnya daftar_nilai = [].
   
2. Fungsi tambah():

   Terima input dari pengguna berupa nama, nim, kelas, dan nilai.
   
   Tambahkan data mahasiswa yang dimasukkan ke dalam daftar daftar_nilai menggunakan append().
   
3. Fungsi tampilkan():

   Jika daftar nilai kosong, tampilkan pesan "Tidak ada data mahasiswa".
   
   Jika tidak kosong, tampilkan header tabel yang berisi kolom Nama, NIM, Kelas, dan Nilai.
   
   Iterasi melalui setiap data mahasiswa dalam daftar_nilai dan tampilkan dalam format tabel.
   
4. Fungsi hapus(nama):

   Cari data mahasiswa berdasarkan nama.
   
   Jika ditemukan, hapus data tersebut dari daftar_nilai menggunakan remove().
   
   Jika tidak ditemukan, tampilkan pesan "Data mahasiswa tidak ditemukan".
   
5. Fungsi ubah(nama, nim_baru, kelas_baru, nilai_baru):

   Cari data mahasiswa berdasarkan nama.
   
   Jika ditemukan, ubah data nim, kelas, dan nilai sesuai input baru.
   
   Jika tidak ditemukan, tampilkan pesan "Data mahasiswa tidak ditemukan".
   
7. Menu utama:

   Tampilkan menu untuk memilih opsi:
   
>Pilihan 1: Tambah data

>Pilihan 2: Tampilkan data

>Pilihan 3: Hapus data

>Pilihan 4: Ubah data

>Pilihan 5: Keluar

8. Selesai:

   Jika pengguna memilih opsi keluar, program selesai.
