nama = "Budi"
umur = 25

# menggabungkan string dapat dilakukan dengan menggunakan tanda +
# jika ingin menggabungkan string maka semua tipe data selain string harus diubah menjadi string terlebih dahulu
# menggunakan function str()

pesan = "Nama Saya " + nama + " Umur " + str(umur)
print(pesan)

# panjang string
panjang_karakter_pesan = len(pesan)
print(panjang_karakter_pesan)

# akses karakter dari sebuah string dengan menggunakan index
# akses karakter menggunakan index urut dari kiri mulai dari index 0
print(nama[0])  # B
print(nama[1])  # u
# akses karakter menggunakan index urut dari belakang mulai dari index -1
print(nama[-1])  # i
print(nama[-2])  # d

# string slice
print(nama[0:2])  # Bu
print(nama[2:])  # di

# string method
# upper()
print(nama.upper())
# lower()
print(nama.lower())
# title()
print(nama.title())
# capitalize()
print(nama.capitalize())
# strip()
print(nama.strip())
# replace()
print(nama.replace("u", "O"))
# count()
print(nama.count("d"))
# find()
print(nama.find("d"))

# string interpolation
# menggunakan keyword "f" sebelum string untuk menggunakan f-string
profil = f"Halo, saya {nama.upper()} umur {umur}"
print(profil)

# menggunakan concatenation
# menggunakan tanda + untuk menggabungkan string, tetapi tipe data pada variabel harus di conversi menjadi string
profil_lama = "Halo, saya " + nama + " Umur " + str(umur)
print(profil_lama)
