a = 10
b = 3

# penjumlahan
print(a + b)

# pengurangan
print(a - b)

# perkalian
print(a * b)

# pembagian
print(a / b)

# pembagian bulat, tanpa desimal
print(a // b)

# modulo, menghasilkan sisa dari pembagian
print(a % b)

# pangkat
print(a ** b)

# compound assignment
print("a awal :", a)

a += 5
print("+=5 :", a)
a -= 5
print("-=5 :", a)
a *= 5
print("*=5 :", a)
a /= 5
print("/=5 :", a)

# STRING OPERATOR
# coba compound assignment pada string
cb_string = "Pesan"
cb_string += " bisa compound assign"
print(cb_string)

# repetisi
print(cb_string * 2)

# membership (in)
print("bisa" in cb_string)
