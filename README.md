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

![image](https://github.com/user-attachments/assets/1847d267-9e47-4192-b42a-e2694b5f8a8e)

Fungsi tampilkan() digunakan untuk menampilkan seluruh data mahasiswa dalam bentuk tabel.

if not daftar_nilai: memeriksa apakah daftar_nilai kosong. Jika kosong, maka akan mencetak pesan bahwa tidak ada data mahasiswa.

Jika ada data mahasiswa, fungsi ini mencetak header tabel dengan kolom: Nama, NIM, Kelas, dan Nilai.

Fungsi menggunakan for data in daftar_nilai: untuk mengiterasi setiap elemen dalam list daftar_nilai dan mencetaknya dalam format yang rapi menggunakan format().

#

![image](https://github.com/user-attachments/assets/bfd3682d-ecf8-40a9-b3cc-0196ea12db74)

Fungsi hapus() digunakan untuk menghapus data mahasiswa berdasarkan nama.

global daftar_nilai digunakan untuk memastikan bahwa perubahan yang dilakukan pada daftar_nilai berlaku di seluruh program.

Fungsi ini akan mengiterasi daftar_nilai dan mencari data mahasiswa yang memiliki nama yang sama dengan parameter nama.

Jika ditemukan, data mahasiswa akan dihapus menggunakan daftar_nilai.remove(data) dan program mencetak pesan bahwa data telah dihapus.

Jika data mahasiswa tidak ditemukan, maka akan mencetak pesan bahwa mahasiswa dengan nama tersebut tidak ditemukan.

#

![image](https://github.com/user-attachments/assets/2f6941a0-f128-4d33-8a5c-853c4a2bb1a1)

Fungsi ubah() digunakan untuk mengubah data mahasiswa berdasarkan nama.

Fungsi ini menerima parameter nama, nim_baru, kelas_baru, dan nilai_baru yang digunakan untuk memperbarui data mahasiswa.

Fungsi akan mencari data mahasiswa dengan nama yang sesuai dan memperbarui nilai-nilai di dalam dictionary tersebut.

Jika data ditemukan dan berhasil diubah, maka akan mencetak pesan bahwa data berhasil diperbarui.

Jika mahasiswa dengan nama tersebut tidak ditemukan, akan mencetak pesan kesalahan.

#

![image](https://github.com/user-attachments/assets/f4bbfcf3-3ae0-46ed-abee-5012c1a7b7fe)

Menu Interaktif:

>Program ini menggunakan loop while True: untuk menampilkan menu interaktif yang memungkinkan pengguna memilih salah satu dari lima opsi:

>Tambah Data: Pengguna diminta untuk memasukkan nama, NIM, kelas, dan nilai mahasiswa yang ingin ditambahkan.

>Tampilkan Data: Menampilkan daftar mahasiswa yang sudah ada.

>Hapus Data: Meminta nama mahasiswa yang ingin dihapus dari daftar.

>Ubah Data: Meminta nama mahasiswa yang ingin diubah, kemudian meminta NIM baru, kelas baru, dan nilai baru.

>Keluar: Keluar dari program dan mencetak pesan "Terima kasih!"

Validasi Pilihan:

Jika pengguna memasukkan pilihan selain 1-5, program akan mencetak pesan "Pilihan tidak valid, silakan coba lagi." dan kembali menampilkan menu.

#

*C. FLOWCHART*

![image](https://github.com/user-attachments/assets/edf23781-df33-4e30-9872-750cc22e2479)

#

*D. HASIL RUN CODE*


