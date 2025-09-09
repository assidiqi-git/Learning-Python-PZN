# set hanya akan menyimpan data unik, tidak ada duplikasi data dalam set
buah = {"jeruk", "mangga", "apel"}
print(buah)

buah.add('mangga')
print(buah)
# set buah tidak akan berubah karena nilai "mangga" sudah ada

buah.remove('mangga')
print(buah)

# dikarenakan set tidak memiliki index maka akses data dalam sebuah set maka tidak bisa diakses melalui index
# untuk akses data dalam set, bisa menggunakan perulangan
for x in buah:
    print(x)
