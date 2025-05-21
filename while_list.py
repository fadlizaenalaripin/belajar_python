"""
Menggunakan While Loop
Anda dapat melakukan pengulangan pada item-item dalam daftar dengan menggunakan whileperulangan.

Gunakan len()fungsi tersebut untuk menentukan panjang daftar, lalu mulai dari 0 dan lakukan pengulangan melalui item daftar dengan merujuk ke indeksnya.

Ingatlah untuk menambah indeks sebesar 1 setelah setiap iterasi.

Contoh
Cetak semua item, menggunakan whileloop untuk menelusuri semua nomor indeks
"""


thislist = ['apple', 'samsung', 'advan']
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1
    