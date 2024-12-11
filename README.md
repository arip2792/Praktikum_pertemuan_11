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

7. Selesai:

   Jika pengguna memilih opsi keluar, program selesai.

#

*B. CODE PROGRAM DAN PENJELASAN*

![image](https://github.com/user-attachments/assets/201373be-2b88-410b-b1fe-65ae68cc32e9)

daftar_nilai adalah list kosong yang digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary. Setiap dictionary akan berisi informasi tentang nama, NIM, kelas, dan nilai mahasiswa
#
![image](https://github.com/user-attachments/assets/39da8d37-3013-402c-81c7-dd22818b0dd0)

Fungsi tambah() digunakan untuk menambahkan data mahasiswa baru ke dalam list daftar_nilai.

Parameter yang diterima adalah:

>nama: Nama mahasiswa

>nim: Nomor Induk Mahasiswa

>kelas: Kelas mahasiswa

>nilai: Nilai mahasiswa

daftar_nilai.append() menambahkan dictionary baru ke dalam list daftar_nilai, dimana dictionary tersebut berisi data mahasiswa.

Fungsi ini mencetak pesan konfirmasi bahwa data mahasiswa berhasil ditambahkan.
#




















