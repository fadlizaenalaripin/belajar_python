thislist = ['apel', 'ceri', 'banana', 'gedang']
# menambahkan item list tanpa harus menghapus salah satu item
thislist.insert(1, 'salak')
# menambah item baru di list langsung di posisi akhir list
thislist.append('pepaya')
# memasukan item ke dalam index yang di tentukan 
thislist.insert(2, 'jeruk')
print(thislist)


this_list = ['salak', 'wortel', 'anggur']
tropical = ['pisang', 'batagor', 'kesemek']
# untuk menghapus item yang di tentukan
this_list.remove('salak')
# Untuk menambahkan elemen dari list lain ke list saat ini, gunakan extend()metode
this_list.extend(tropical)
print(this_list)

"""
Metode ini extend()tidak harus menambahkan daftar ,
Anda dapat menambahkan objek apa pun yang dapat diulang (tupel, set, dict dll.).
contoh:
"""
ini_list = ['ikan', 'beruang']
ini_tuple = ('harimau', 'singa')

ini_list.extend(ini_tuple)
print(ini_list)

"""
    Metode ini pop()menghapus indeks yang ditentukan.
    ka Anda tidak menentukan indeks, pop()metode akan menghapus item terakhir.
"""

contoh_pop = ['x', 'y', 't']
contoh_pop.pop(1)
print(contoh_pop)

"""
Kata delkunci juga menghapus indeks yang ditentukan
Hapus item pertama:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
Kata delkunci juga dapat menghapus daftar sepenuhnya.

Contoh
Hapus seluruh daftar:

thislist = ["apple", "banana", "cherry"]
del thislist
"""

untuk_del = ['t', 'y', 'b']
del untuk_del

"""
Metode ini clear()mengosongkan daftar.
Daftarnya masih tetap ada, tetapi tidak ada isinya.
"""
thislist2 = ["apple", "banana", "cherry"]
thislist2.clear()
print(thislist2)