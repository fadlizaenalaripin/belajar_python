# untuk mengubah tuple dan menambahkan nilai ke tuple anda dapat mengubah nya lebih dulu ke list 
# lalu menambahkan nilai nya trus merubah list nya lagi ke tuple contoh

x = ("apple", "banana", "salak", "jeruk")
y = list(x)
# menambahkan item baru di index ke 2 lalu mengubahnya lagi ke tuple
y.insert(2,"nanas")
# mengganti item di index tertentu
y [1] = "kiwi"
# menghapus item di list lalu di rubah nya di tuple lagi
y.remove("apple")
x = tuple(y)

print(x)

print()
"""
Tambahkan Item
Karena tupel tidak dapat diubah, tupel tidak memiliki metode bawaan append(), tetapi ada cara lain untuk menambahkan item ke tupel.

1. Ubah menjadi daftar : Sama seperti solusi untuk mengubah tupel, Anda dapat mengubahnya menjadi daftar, menambahkan item Anda, dan mengubahnya kembali menjadi tupel.

Contoh
Ubah tuple menjadi daftar, tambahkan "orange", dan ubah kembali menjadi tuple:
"""
thistuple = ("apple", "banana", "cherry")
a = list(thistuple)
a.append("orange")
thistuple = tuple(a)
# menghapus tuple sepenuh nya 
# del thistuple kalo eror berarti udh ke apus
print(thistuple)

"""
2. Tambahkan tuple ke tuple . Anda diperbolehkan menambahkan tuple ke tuple, jadi jika Anda ingin menambahkan satu item (atau banyak), buat tuple baru dengan item tersebut, dan tambahkan ke tuple yang sudah ada:

Contoh
Buat tupel baru dengan nilai "orange", dan tambahkan tupel tersebut:
"""
inituple = ("apple", "banana", "chery")
z = ("salak",)
inituple +=z
print(inituple)