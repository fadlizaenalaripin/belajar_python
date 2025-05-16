buah_tuple = ('mangga', 'banana','ceri')
print(type(buah_tuple))

buah_list = list(buah_tuple)
# menambahkan list
buah_list.append('watu')
# mengubah list
buah_list [1] = "kecipir"
print(type(buah_list))
print(buah_list)

this_list = ('buah', 'motor', 'nangka', 'ceri', 'banana')
# mengambil sebagian isi list contoh dari 1 sampai sebelum 4
print(this_list[1:4])
# mengambil item list dari mulai awal sampai dengan sebelum 2
print(this_list[:2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist [2:4] = "salak", ""
# mengecek apakah apple ada di dalam list
if "apple" in thislist:
    print("ya apple ada di list bro")
#Dengan menghilangkan nilai akhir, rentang akan berlanjut hingga akhir list
print(thislist[2:])

ini_list = ['apel', 'banana', 'ceri', 'salak']
ini_list [1] = "blekicot"
print(ini_list)