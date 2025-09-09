def ambil_soal():
    soal_asli = []
    try:
        with open('file/bank_soal.txt', 'r') as file:
            for line in file:
                soal_asli.append(line.strip())
    except FileNotFoundError:
        print("file file not found")
    except PermissionError:
        print("permission error")
    except:
        print("read file error")
    return soal_asli


def buat_soal():
    import random
    soal_asli = ambil_soal()

    # acak soal
    random.shuffle(soal_asli)
    soal_ujian = []
    for soal in soal_asli:
        data = soal.split("|")  # ["pertanyaan", "jawaban1,jawaban2,jawaban3,jawaban4"]
        pertanyaan = data[0]  # pertanyaan
        jawaban = data[1].split(",")  # ["jawaban1","jawaban2","jawaban3","jawaban4"]
        jawaban_benar = jawaban[0]  # jawaban1

        # acak urutan jawaban
        random.shuffle(jawaban)

        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })

    return soal_ujian


def ujian():
    soal_ujian = buat_soal()
    opsi = ["A", "B", "C", "D"]
    jawaban_benar = 0
    jawaban_salah = 0
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print(f"{i + 1}. Pertanyaan : {soal['pertanyaan']}")
        print(f"Jawaban :")
        terjawab = False
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j], ". ", jawaban)

        while terjawab == False:
            try:
                jawaban_user = input("Jawaban : ")
                jawaban_user_index = opsi.index(jawaban_user.upper())
                jawaban_asli_user = soal["jawaban"][jawaban_user_index]

                if jawaban_asli_user == soal["jawaban_benar"]:
                    print("Jawaban Benar")
                    jawaban_benar += 1
                else:
                    print("Jawaban Salah")
                    jawaban_salah += 1
                terjawab = True
            except:
                print("Pilihan yang dimasukkan tidak sesuai")
    print("Hasil Ujian")
    print("Jawaban Benar : ", jawaban_benar)
    print("Jawaban Salah : ", jawaban_salah)
    print("Hasil Ujian : ", jawaban_benar / (jawaban_benar + jawaban_salah) * 100, "%")


ujian()
