thislist = ['banana', 'pepaya', 'anggur']
for x in thislist [::-2]:
    print(x)
    
    
"""
Ulangi Melalui Nomor Indeks
Anda juga dapat menelusuri item list dengan merujuk pada nomor indeksnya.
Gunakan fungsi range()dan len()untuk membuat iterable yang sesuai.
"""

this_list = ['pisang', 'semangka', 'pepaya','anggur']
for i in range(len(this_list)):
    print(this_list[i])
    
    
"""
menggunakan for pendek dan simpel
"""

list = ['ceri','banana','semangka']
[print (x) for x in list]
    

"""
emahaman Daftar
Pemahaman daftar menawarkan sintaksis yang lebih pendek saat Anda ingin membuat daftar baru berdasarkan nilai daftar yang ada.

Contoh:

Berdasarkan daftar buah-buahan, Anda menginginkan daftar baru yang hanya berisi buah-buahan dengan huruf "a" dalam namanya.

Tanpa pemahaman daftar, Anda harus menulis forpernyataan dengan pengujian kondisional di dalamnya:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


"""
Dengan pemahaman daftar, Anda dapat melakukan semua itu hanya dengan satu baris kode:
"""

fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]
# untuk mengambil item yang ada huruf a nya saja
newlist2 = [x for x in fruits if "a" in x]
# untuk mengambil item kecuali item apple
newlist3 = [x for x in fruits2 if x != "apple"]
# untuk mengambil semua item trus di jadikan kapital semua
newlist4 = [x.upper() for x in fruits2]
# untuk mengubah item nya menejadi hello di list baru
newlist5 = ['hello' for x in fruits2]
# Mengubah Item Tertentu Saja (Pakai if else di bagian depan
newlist6 = [x if x != 'banana' else 'orange' for x in fruits2]
print(newlist6)
print(newlist5)
print(newlist4)
print(newlist3)
print(newlist2)