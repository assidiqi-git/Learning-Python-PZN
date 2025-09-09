# mode file io
# r (read)-> membaca file yang sudah ada
# w (write)-> menulis file baru atau menimpa file dengan nama yang sama
# a (append)-> menambah data di akhir file
# x (create)-> membuat file baru, akan error jika file yang sama sudah ada

# print("simpan data nilai")
#
# file = open("file/nilai-siswa.txt", "w")
#
# while True:
#     nama = input("nama: ")
#     if nama == "":
#         break
#     nilai = input("nilai: ")
#
#     file.write(f"{nama},{nilai}\n")
#     print(f"nama: {nama} dengan nilai: {nilai} berhasil disimpan")
#
# file.close()
# print("program selesai")

# membaca file
# print("menampilkan data nilai")
# file = open("file/nilai-siswa.txt", "r")
#
# for line in file:
#     data = line.strip().split(',')
#     print(f"{data[0]} : {data[1]}")
#
# file.close()
#
# print("program selesai")


# menggunakan "with" dalam interaksi dengan file
# sehingga kita tidak perlu khawatir jika lupa untuk menutup file
# print("menampilkan nilai siswa")
# with open("file/nilai-siswa.txt", "r") as file:
#     for line in file:
#         data = line.strip().split(',')
#         print(f"{data[0]} : {data[1]}")
# print("program selesai")

# error handling file
print("menampilkan nilai siswa")
try:
    with open("nilai-siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(',')
            print(f"{data[0]} : {data[1]}")
except FileNotFoundError:
    print("file tidak ditemukan")

print("program selesai")
