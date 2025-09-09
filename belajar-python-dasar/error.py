# try-except
# print("===== KALKULATOR ======")
#
# try:
#     angka1 = int(input("angka1: "))
#     angka2 = int(input("angka2: "))
#     hasil = angka1 * angka2
#     print(hasil)
#
# except ValueError:
#     print("Mohon masukkan angka yang valid")
# except ZeroDivisionError:
#     print("input tidak boleh 0")
# except:
#     print("error dalam perhitungan")
#
# print("===== KALKULATOR SELESAI ======")

# try-except-else
try:
    angka = int(input("angka: "))
except ValueError:
    print("angka tidak valid")
else:  # hanya akan dijalankan jika tidak terdapat error
    print("angka valid")
    if angka > 0:
        print("angka positif")
    elif angka < 0:
        print("angka negatif")
    else:
        print("angka 0")
finally:  # selalu dijalankan baik ada error maupun tidak
    print("program selesai")
