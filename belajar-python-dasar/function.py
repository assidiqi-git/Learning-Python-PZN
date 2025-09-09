# membuat function menggunakan keyword "def"
# penamaan function menggunakan snake_case

def nama_function():
    # body function
    print("ini sebuah function")


nama_function()


# penulisan function dengan parameter
def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar  # local variable
    print("Luas persegi panjang: ", luas)


hitung_luas_persegi_panjang(100, 100)

# keyword argument, sebuah cara untuk memberikan parameter/argument saat pemanggilan function
# agar tidak selalu mengikuti urutan dari function
# dapat dilakukan dengan cara menyebutkan nama parameternya
hitung_luas_persegi_panjang(lebar=10, panjang=102)


# default value parameter
def sapa(nama, sapaan="Halo"):
    print(sapaan, nama)


sapa("Saya")


# function dengan return value
def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius * radius
    return luas


luas_lingkaran = hitung_luas_lingkaran(10)
print(luas_lingkaran)

# global variable
nama_global = "Bwuko"


def tampilkan_nama():
    print("tampilkan nama ", nama_global)


def ubah_nama():
    global nama_global
    nama_global = "Bob"
    print("ubah nama ", nama_global)


tampilkan_nama()
ubah_nama()
tampilkan_nama()


# dynamic parameters
# menggunakan * untuk mengubah seluruh parameter yang diberikan
# saat akses function untuk mengubah semua parameter yang diberikan menjadi sebuah list
def cetak_list(*list):
    print(list)
    print(f"tipe {type(list)}")
    for item in list:
        print(item)


def cetak_dict(**dict):
    print(dict)
    print(f"tipe {type(dict)}")
    for key, value in dict.items():
        print(f"{key} = {value}")


cetak_list(1, 2, 3, 4, 5, 6)
cetak_dict(nama="Bwuko", kota="banjarmasin")
