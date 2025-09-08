# if
angka = int(input("angka: "))

if angka > 0:
    print(f"{angka} adalah angka positif")

if angka < 0:
    print(f"{angka} adalah angka negatif")

if angka == 0:
    print(f"{angka} adalah angka 0")

# elif (else-if)
if angka >= 90:
    print("Grade A")
elif angka >= 80:
    print("Grade B")
elif angka >= 70:
    print("Grade C")
elif angka >= 60:
    print("Grade D")
else:
    print("Grade E")

# if-else
if angka > 60:
    print(f"Anda Lulus")
else:
    print(f"Anda Tidak Lulus")
