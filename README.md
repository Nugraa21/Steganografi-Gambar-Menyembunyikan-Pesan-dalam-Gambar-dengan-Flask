# Steganografi Gambar - Penyisipan Pesan dalam Gambar

![Logo](https://img.shields.io/badge/Project%20by-nugra21-%23FF5733)  
![Python](https://img.shields.io/badge/Python-3.9-%233776AB) ![Flask](https://img.shields.io/badge/Flask-2.0-%23D90060) ![Pillow](https://img.shields.io/badge/Pillow-8.2-%23F7796B)

## Deskripsi Proyek

Proyek ini bertujuan untuk membuat aplikasi web menggunakan Flask yang dapat melakukan steganografi gambar, yaitu menyisipkan pesan teks ke dalam gambar tanpa mengubah secara signifikan tampilan gambar tersebut. Pengguna dapat mengupload gambar dan memasukkan pesan untuk disembunyikan, serta membaca kembali pesan tersembunyi tersebut dengan mengupload gambar yang sudah disisipkan pesan.

### Tentang Pembuat
- **Nama**: Ludang Prasetyo Nugroho  
- **Username**: [nugra21](https://github.com/nugra21)  
- **Channel YouTube**: [nugra21](https://youtube.com/nugra21)  
- **Website**: [nugra.online](https://nugra.online)

#### Copyright & Lisensi
© 2025 Ludang Prasetyo Nugroho. Semua hak dilindungi oleh hukum.  
Proyek ini dilisensikan di bawah [MIT License](https://opensource.org/licenses/MIT).

---


## Struktur File

```bash
/steganografi
├── /static
│   └── /uploads          # Folder untuk menyimpan gambar yang diupload
├── /templates
│   ├── index.html        # Halaman utama untuk memasukkan gambar dan pesan
│   └── decode.html       # Halaman untuk mendekode pesan dari gambar
├── app.py                # Script utama Flask yang menjalankan server web
├── requirements.txt      # Daftar dependensi yang dibutuhkan oleh aplikasi
└── README.md             # Dokumentasi proyek

```
### Penjelasan Struktur File

1. /static/uploads: Folder ini digunakan untuk menyimpan gambar yang diupload oleh pengguna, baik gambar asli maupun gambar yang sudah disisipkan pesan.

2. /templates/index.html: Halaman utama yang menampilkan form untuk meng-upload gambar dan memasukkan pesan yang ingin disembunyikan.

3. /templates/decode.html: Halaman untuk menampilkan pesan yang terdekripsi dari gambar yang di-upload.

4. app.py: Script Python utama yang menggunakan Flask untuk mengatur routing, menerima file upload, dan memproses gambar dengan menyisipkan/membaca pesan.

5. requirements.txt: File ini berisi daftar dependensi yang dibutuhkan untuk menjalankan aplikasi (Flask, Pillow, dll).

## Cara Menjalankan Aplikasi

1. Instal Dependensi:
Pastikan Python dan pip terinstal, lalu jalankan perintah ini di termina
    ```bash
    pip install -r requirements.txt
    ```

2. Jalankan Server Flask:
Di terminal, arahkan ke folder proyek dan jalankan
    ```bash
    python app.py
    ```
3. Akses Aplikasi:
Buka browser dan akses aplikasi di
    ```bash
    http://127.0.0.1:5000/
    
    ```




## Teknologi yang Digunakan

1. Python: Bahasa pemrograman yang digunakan untuk pengembangan backend aplikasi.

2. Flask: Framework Python yang digunakan untuk membangun aplikasi web ini.

3. Pillow (PIL): Library Python untuk memproses gambar, yang digunakan untuk menyisipkan dan mengekstrak pesan dari gambar.

4. HTML, CSS: Digunakan untuk tampilan antarmuka pengguna (front-end).

5. JavaScript: Untuk beberapa interaksi tambahan pada form HTML.

6. Werkzeug: Digunakan oleh Flask untuk menangani file upload.

## Cara Kerja

### Aplikasi ini bekerja dengan prinsip dasar Least Significant Bit (LSB), yaitu menyembunyikan data dalam bit terakhir dari nilai warna pada pixel gambar.

Proses Enkripsi (Menyisipkan Pesan)
1. Pengguna meng-upload gambar dan memasukkan pesan yang ingin disembunyikan.

22. Pesan tersebut dikonversi menjadi format biner (bit).

3. Bit pesan akan disisipkan ke dalam bit terakhir (LSB) pada kanal merah (R) dari setiap pixel gambar.

4. Hasilnya adalah gambar yang secara visual tidak berubah, namun pesan telah tersimpan dalam bit LSB pixel-pixelnya.

Proses Dekripsi (Membaca Pesan)

1. Pengguna meng-upload gambar yang sudah diproses.

2. Aplikasi akan membaca bit terakhir dari kanal merah setiap pixel.


## Prinsip Steganografi

    Steganografi adalah teknik untuk menyembunyikan pesan dalam media lain (dalam hal ini gambar), sehingga pesan tersebut tidak dapat terlihat dengan kasat mata. Prinsip dasar yang digunakan dalam proyek ini adalah Least Significant Bit (LSB). Teknik ini mengganti bit terakhir (bit yang paling tidak signifikan) dalam representasi warna RGB dari gambar dengan bit pesan yang ingin disembunyikan.

## Teori

>Binary Encoding: Pesan teks diubah menjadi representasi biner dengan menggunakan kode ASCII. Setiap karakter akan diubah menjadi byte (8-bit).

>LSB (Least Significant Bit): Dengan mengganti bit terakhir dari komponen warna (RGB), perubahan yang terjadi pada gambar sangat kecil, sehingga hampir tidak terdeteksi oleh mata manusia.

>Penggunaan RGB: Gambar diubah menjadi format RGB, dan hanya kanal merah (Red) yang digunakan untuk menyisipkan data pesan. Setiap pixel gambar terdiri dari tiga kanal warna (R, G, B), di mana nilai kanal merah (R) akan diubah sedikit untuk menyimpan pesan.

## Teori dan Penjelasan Praktis

### Teori

>Konversi Teks ke Biner: Setiap karakter dalam pesan dikonversi menjadi kode ASCII 8-bit, kemudian concatenated untuk membentuk string biner dari pesan.

>Steganografi LSB: Teknik ini memodifikasi bit terakhir dari komponen warna pada gambar. Misalnya, jika pixel memiliki nilai merah 255 (11111111 dalam biner), bit terakhir bisa diganti dengan bit pesan (misalnya 0 atau 1).

### Praktek

#### Pada implementasi aplikasi ini:

1. Encoding (Penyisipan Pesan): Kita menyisipkan bit pesan ke dalam bit terakhir nilai merah (R) dari setiap pixel dalam gambar.

2. Decoding (Pembacaan Pesan): Kita membaca bit terakhir dari nilai merah pixel-pixel gambar untuk mengembalikan pesan yang tersembunyi.

> Dengan teknik ini, gambar yang telah disisipkan pesan tetap terlihat hampir sama dengan gambar aslinya, namun dapat mengandung informasi yang disembunyikan secara aman.