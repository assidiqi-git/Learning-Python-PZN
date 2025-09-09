def menu():
    while True:
        print("=== TEBAK ANGKA ===")
        print("1. Tebak Angka")
        print("2. Keluar")

        try:
            pilihan = int(input("pilihan : "))
            if pilihan == 1:
                tebak_angka()
            elif pilihan == 2:
                print("Program Selesai")
                break
            else:
                print("Pilihan tidak sesuai")
        except ValueError:
            print("input salah, harus berupa angka")


def tebak_angka():
    import random
    target = random.randint(1, 10)
    max_kesempatan = 3
    tebakan = 0
    while tebakan < max_kesempatan:
        try:
            angka_user = int(input("angka : "))
            tebakan += 1
            if angka_user > target:
                print("angka terlalu besar")
            elif angka_user < target:
                print("angka terlalu kecil")
            else:
                print("tebakan anda benar")
                break
        except ValueError:
            print("input salah, harus berupa angka")
    else:
        print("kamu telah melewati maksimal kesempatan")
        print(f"angka acak adalah {target}")


menu()
