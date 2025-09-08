password_benar = "123"
percobaan = 0
max_percobaan = 3

while percobaan < max_percobaan:
    password = input("Password: ")
    percobaan += 1

    if password == password_benar:
        print("login berhasil")
        break
    else:
        print("password salah, sisa percobaan:", max_percobaan - percobaan)
else:
    print("terlalu banyak percobaan gagal. akses ditolak")
