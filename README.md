# Dokumentasi Postest 1 Algoritma dan Struktur Data 
Muhammad irfan Maulana (2209116036)

dibuat untuk memenuhi penugasan praktikum 1 Algoritma dan struktur data

# Pembahasan dan visualisasi Algoritma (Mergesort dan Quicksort)

## Quicksort
Quicksort adalah suatu teknik sortir yang menggunakan algoritma divide and conquer yaitu pembagian suatu masalah menjadi bagian bagian kecil agar lebih mudah dalam penyelesaiannya. Cara kerja quicksort adalah dengan menentukan pivot dari suatu data yang kemudian yang menjadi titik tengah pembagian partisi - partisi data, menjadi partisi kanan, dan kiri.
kemudian elemen yang lebih kecil dari pivot dipindahkan kesebelah kiri pivot dan elemen yang lebih besar dipindahkan di sebelah kanan pivot. data akan menjadi terpecah dan kemudian terurut.

### Visualisasi Quicksort
![Diagram Tanpa Judul drawio (8)](https://user-images.githubusercontent.com/121864328/222624436-27e909ff-445b-44e9-b68c-888883d64fae.png)

### implementasi program dan penjelasan

![image](https://user-images.githubusercontent.com/121864328/222623497-b8f601ec-a105-4f5e-830f-4b2f6acd6c81.png)

pada gambar diatas terdapat library random yaitu untuk mendapatkan sebuah kumpulan angka acak yang akan menjadi bahan sorting. Fungsi tambah adalah fungsi untuk mencari angka random yang akan selalu berbeda setiap program dirun.

![image](https://user-images.githubusercontent.com/121864328/222625293-0a4e40db-a5dd-4ba0-ab7c-dca913cd2740.png)

pada gambar diatas terdapat fungsi partition yaitu untuk melakukan pembagian partisi - partisi.

![image](https://user-images.githubusercontent.com/121864328/222626310-ee9e3df4-7a28-4703-bf85-9810b2f15166.png)

fungsi quicksort adalah fungsi untuk membandingkan besar data.

## Mergesort

Mergesort adalah algoritma sortir yang caranya adalah memecah data menjadi bagian - bagian dan dibandingkan besarannya. berbeda dengan quicksort, mergesort lebih sederhana.

### Visualisasi Quicksort

![Diagram Tanpa Judul drawio (9)](https://user-images.githubusercontent.com/121864328/222635243-53fc858a-49b4-4ade-bb7d-85837e51f175.png)

### Implementasi program dan penjelasan

![image](https://user-images.githubusercontent.com/121864328/222638619-6869f26c-5595-4e49-bf84-74db47a440e6.png)

sama seperti quicksort, menggunakan library random untuk menentukan bilangan acak sebagai data

![image](https://user-images.githubusercontent.com/121864328/222638716-c18a73a9-0f25-4592-8534-5ee5c06c9dc3.png)

fungsi mergesort untuk membagi partisi kanan dan kiri sekaligus mengsortir data yang disimpan dalam list data bernama arr.

![image](https://user-images.githubusercontent.com/121864328/222638936-836d2362-36aa-4cb5-916a-42f8c12465fc.png)

fungsi untuk print isi data arr.





