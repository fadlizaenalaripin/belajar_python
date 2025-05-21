mytuple = ('banana', 'pisang', 'ceri')
print(type(mytuple))
print(mytuple[0])

print()

# tuple dengan satu item 
# kalo kita bikin tuple dengan satu item harus pake komo kalo ga nanti bakal di anggap str

t1 =('apple',)
print(type(t1))

t2 =('apple')
print(type(t2))

print()
# tuple jga bisa berisi data campuran 

campuran = ('apple', 2, 12.5, True)
print(type(campuran))
# mengecek seberapa panjang tuple
print(len(campuran))
print(campuran)

"""
🔨 Cara Membuat Tuple
Cara	Contoh
Manual	tup = ("a", "b", "c")
Pakai constructor	tup = tuple(("a", "b", "c"))

🤔 Jadi, bedanya apa?
Cara	Kapan dipakai	Kelebihan
Manual	Kalau kamu udah tahu isinya langsung	Cepat dan ringkas
Constructor tuple()	Kalau datanya berasal dari tipe lain	Lebih fleksibel dan bisa konversi

"""

print()

# contoh penggunaan yang tepat untuk constructor

thislist = ['apple', ' banana', 'pisang']
thistuple = tuple(thislist) # mengonverensi list dan mengambil item nya ke ke dalam variabel baru bertipe tuple
# mengakses tuple menggunakan index posisitif
print(thislist[0])
print(thislist[-2])
print(thistuple)


# menggunakan rentang index di tuple
inituple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# menggunakan rentang index contoh
# dari index ke 2 sampai sebelum index ke 5 berarti 4
print(inituple[2:5])

# dengan tidak menggunakan nilai awal rentang akan di mulai pada item pertama 
# contoh
tuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple2[:4])
# dengan menghilangkan nilai akhir rentang akan berlanjut hingga nilai akhir tuple contoh
print(tuple2[3:])
print("di bawah ini bagian rentang index negatif")
# ini bagian rentang index negatif 
# contoh ini mengembalikan item dari indeks -4 (termasuk) ke indeks -1 (dikecualikan)
print(tuple2[-4:-1])

print()
# untuk mengecek apakah suatu item ada di dalam tupe gunakan in kata kunci
if "apple" in tuple2:
       print("yes apple in here")
else:
    print("l dont now")