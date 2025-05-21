# mengurutkan naik berdasarkan abjd dari A-Z
print('ini bagian abjad')
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print()
# mengurutkan berdasrkan nomor dari yang terkecil sampai terbesar
print('ini bagian angka')
inilist = [100, 50, 65, 82, 23]
inilist.sort
print(inilist)

print()
# descending abjad
print('ini bagian descending abjd')
listdes = ["orange", "mango", "kiwi", "pineapple", "banana"]
listdes.sort(reverse=True)
print(listdes)

print()
# bagian angka
print('ini bagian descending angka')
listangkades = [100, 50, 65, 82, 23]
listangkades.sort(reverse=True)
print(listangkades)

print()

"""
Sesuaikan Fungsi Sortir
Anda juga dapat menyesuaikan fungsi Anda sendiri dengan menggunakan argumen kata kunci .key = function

Fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu):

Contoh
Urutkan daftar berdasarkan seberapa dekat angka tersebut dengan 50:
"""
# bagian fungsi
print("bagian fungsi")
def myfunc(angka):
    return abs(angka - 50)
listfunc = [100, 50, 65, 82, 23]
listfunc.sort(key=myfunc)
print(listfunc)

print()

# bagian case sensitive
# di urutkan berdasarkan huruf besar terlebih dahulu

thelist = ["banana", "Orange", "Kiwi", "cherry"]
thelist.sort()
print(thelist)

print()

"""
🔍 Penjelasan:
key=str.lower artinya:

Saat mengurutkan, semua huruf dianggap huruf kecil dulu ➜ jadi adil

Contoh:

'Orange' ➜ 'orange'

'Kiwi' ➜ 'kiwi'

'banana' ➜ 'banana'

'cherry' ➜ 'cherry'
"""

# bagian insensitiv jadi semua huruf di ubah menjadi kecil trus di urutkan berdasarkan A-Z
print('ini bagian insesnsitive')
inlist = ["banana", "Orange", "Kiwi", "cherry"]
inlist.sort(key=str.lower)
print(inlist)

print()

# ini bagian reverse order 
# jadi membalikan posisi item list yang tadinya ada di depan jadi di urutan belakang 
# misal "a b c" maka akan menjadi "c b a"

print("bagian reverse order")
relist = ["banana", "Orange", "Kiwi", "cherry"]
relist.reverse()
print(relist)