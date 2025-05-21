"""
Salin Daftar
Anda tidak dapat menyalin daftar hanya dengan mengetik list2 = list1,
karena: list2hanya akan menjadi referensi ke list1, dan perubahan yang dibuat
dalam list1akan secara otomatis juga dibuat dalam list2.
"""
thislist = ['banana', 'ceri', 'melon', 'pisang']
mylist = thislist.copy()
mylist.append('semangka')
print(mylist)
print(thislist)

"""
. Menggunakan list()
Fungsi list() juga membuat salinan baru dari list yang lama.
"""
print()


list1 = ['cirebon', 'bandung', 'sumendang', 'brebes']
list2 = list(list1)
list2.append('jakarta')
print(list1)
print(list2)


"""
3. Menggunakan Irisan (Slice) [:]
Operator irisan (slice) [:] artinya ambil semua isi dari list.
"""

list3 = ['cirebon', 'bandung', 'sumendang', 'brebes']
list4 = list3[:]
print(list4)