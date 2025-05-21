"""
Python - Gabung Daftar
Gabungkan Dua Daftar
Ada beberapa cara untuk menggabungkan, atau menyatukan, dua atau lebih daftar dalam Python.

Salah satu cara termudah adalah dengan menggunakan + operator.
"""

list1 = ['a', 'b', 'c']
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

print()
# ini pakai for 

thislist = ['a','b','c'] 
mylist = [1,2,3]
for x in thislist: # setiap item di dalam thislist ('a', 'b', 'c') 
    mylist.append(x) # tambahkan ke mylist satu persatu 
print(mylist)

print()

# menggunakan extend()

list3 = ['a', 'b', 'c']
list4 = [1,2,3]
list3.extend(list4)
jumlah = list3.count('a')
print("Jumlah huruf 'a':", jumlah)
print("jumlah item list: ", list3)

"""
| **Method**  | **Artinya**                                                                      | **Contoh**                        |
| ----------- | -------------------------------------------------------------------------------- | --------------------------------- |
| `append()`  | Menambahkan **1 item** ke akhir list.                                            | `list.append("apel")`             |
| `clear()`   | Menghapus **semua isi** dalam list (jadi kosong).                                | `list.clear()`                    |
| `copy()`    | Membuat **salinan list baru** (tidak terhubung ke aslinya).                      | `newlist = list.copy()`           |
| `count()`   | Menghitung **berapa kali** suatu nilai muncul di list.                           | `list.count("apel")`              |
| `extend()`  | Menambahkan **semua item dari list lain** ke list yang sekarang.                 | `list.extend(["jeruk", "melon"])` |
| `index()`   | Mengembalikan **posisi/index** pertama dari suatu nilai.                         | `list.index("pisang")`            |
| `insert()`  | Menyisipkan item ke **posisi tertentu** dalam list.                              | `list.insert(1, "anggur")`        |
| `pop()`     | Menghapus item **berdasarkan posisi** (default: terakhir), dan mengembalikannya. | `list.pop()` atau `list.pop(0)`   |
| `remove()`  | Menghapus **item pertama** yang cocok dengan nilai yang ditentukan.              | `list.remove("apel")`             |
| `reverse()` | Membalik urutan item di list (depan jadi belakang).                              | `list.reverse()`                  |
| `sort()`    | Mengurutkan item dalam list (secara naik/abjad).                                 | `list.sort()`                     |

"""