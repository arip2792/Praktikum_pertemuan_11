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

#

PENJELASAN :

![image](https://github.com/user-attachments/assets/0ff6dbdc-17e6-4f01-9882-80d7aebdf0a9)

__init__(self) adalah metode yang dijalankan otomatis ketika kita membuat objek dari kelas SistemMahasiswa. Di dalam metode ini, kita membuat atribut __daftar_mahasiswa yang berupa dictionary kosong. Dictionary ini akan digunakan untuk menyimpan data mahasiswa, di mana nama mahasiswa menjadi kunci (key), dan informasi seperti NIM, nilai, dan status menjadi nilai (value).
#
![image](https://github.com/user-attachments/assets/5e0fc611-d56b-468f-84d0-cca656ccbab9)

tambah(self, nama, nim, nilai): Metode ini digunakan untuk menambahkan mahasiswa ke dalam daftar __daftar_mahasiswa.

Validasi Nama: Nama mahasiswa harus memiliki minimal 3 karakter. Jika tidak, program menampilkan pesan error.

Cek Duplikasi Nama: Sebelum menambahkan, sistem memeriksa apakah nama mahasiswa sudah ada di dalam daftar. Jika sudah ada, tampilkan pesan kesalahan.

Menentukan Status Mahasiswa: Berdasarkan nilai yang dimasukkan, status mahasiswa ditentukan:

   >Nilai >= 85 → "Cumlaude"

   >Nilai >= 75 → "Sangat Baik"

   >Nilai >= 60 → "Baik"

   >Nilai < 60 → "Perlu Perbaikan"

Menyimpan Data Mahasiswa: Setelah validasi dan penentuan status, data mahasiswa disimpan dalam dictionary __daftar_mahasiswa dengan nama mahasiswa (huruf kecil) sebagai kunci.
#
![image](https://github.com/user-attachments/assets/40a3d807-ba8b-4ba1-95c4-e945e41d6251)

tampilkan(self): Metode ini digunakan untuk menampilkan semua data mahasiswa yang ada dalam sistem.

Cek Kosong: Sebelum menampilkan, program memeriksa apakah daftar mahasiswa kosong. Jika kosong, tampilkan pesan "Tidak ada data mahasiswa."

Format Tampilan: Menampilkan nama, NIM, nilai, dan status mahasiswa dalam format tabel yang teratur. Nama mahasiswa ditampilkan dengan format huruf kapital pertama (title()).
#
![image](https://github.com/user-attachments/assets/f1f43e5b-758d-4fa6-a911-56a8a39c68b1)

hapus(self, nama): Metode ini digunakan untuk menghapus mahasiswa dari daftar berdasarkan nama.

Nama diubah menjadi huruf kecil: Nama yang dimasukkan oleh pengguna diubah menjadi huruf kecil agar pencocokan nama tidak tergantung pada huruf kapital.

Cek Keberadaan Nama: Jika nama mahasiswa ada dalam daftar, maka data mahasiswa tersebut akan dihapus. Jika tidak ada, tampilkan pesan bahwa mahasiswa tidak ditemukan.
#
![image](https://github.com/user-attachments/assets/6005acf7-36b5-44c7-96af-1dbff861f6c0)

ubah(self, nama): Metode ini digunakan untuk mengubah data mahasiswa, baik NIM atau nilai.

Cek Keberadaan Mahasiswa: Jika nama mahasiswa tidak ditemukan dalam daftar, tampilkan pesan kesalahan.

Pilihan Pengguna: Pengguna diberikan dua pilihan untuk mengubah data: 1) NIM atau 2) Nilai.

Ubah NIM: Jika pengguna memilih untuk mengubah NIM, sistem meminta input NIM baru dan memperbarui data.

Ubah Nilai: Jika memilih untuk mengubah nilai, sistem meminta input nilai baru, memvalidasi agar berada dalam rentang 0-100, dan memperbarui nilai serta status mahasiswa berdasarkan nilai baru.
#
![image](https://github.com/user-attachments/assets/f3395048-afa5-4531-9297-fe8f13631498)

main(): Fungsi utama yang menjalankan program.

Membuat Objek sistem: Membuat objek dari kelas SistemMahasiswa.

Menampilkan Menu: Program menampilkan menu utama untuk pengguna memilih tindakan yang ingin dilakukan.

Pengguna Memilih Menu: Berdasarkan input pilihan pengguna, program akan memanggil metode yang sesuai (tambah, tampilkan, hapus, atau ubah).

Keluar: Jika pengguna memilih opsi kelima, program akan berhenti dan menampilkan pesan terima kasih
