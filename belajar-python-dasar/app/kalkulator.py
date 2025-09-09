def penjumlahan():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 + angka2
        print(hasil)
    except ValueError:
        print("input harus angka")
    except:
        print("operasi error")


def pengurangan():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 - angka2
        print(hasil)
    except ValueError:
        print("input harus angka")
    except:
        print("operasi error")


def perkalian():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 * angka2
        print(hasil)
    except ValueError:
        print("input harus angka")
    except:
        print("operasi error")


def pembagian():
    try:
        angka1 = int(input("angka 1: "))
        angka2 = int(input("angka 2: "))
        hasil = angka1 / angka2
        print(hasil)

    except ValueError:
        print("input harus angka")
    except ZeroDivisionError:
        print("input tidak boleh 0")
    except:
        print("operasi error")


def menu():
    while True:
        print("===== KALKULATOR SEDERHANA =====")
        print("1. penjumlahan")
        print("2. pengurangan")
        print("3. perkalian")
        print("4. pembagian")
        print("5. keluar")
        print("===== KALKULATOR SEDERHANA =====")

        try:
            pilihan = int(input("pilihan: "))
            if pilihan == 1:
                penjumlahan()
            elif pilihan == 2:
                pengurangan()
            elif pilihan == 3:
                perkalian()
            elif pilihan == 4:
                pembagian()
            else:
                print("sampai jumpa")
                break
        except ValueError:
            print("input harus berupa angka, sesuai pilihan")


menu()
