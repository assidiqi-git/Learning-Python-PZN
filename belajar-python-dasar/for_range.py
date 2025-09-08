# perulangan menggunakan range dimulai dari index 0
for i in range(5):
    print("hello")
    print(i)

# memulai index dari 1 bukan dari 0
for i in range(1, 6):
    print("hello")
    print(i)

# perhitungan mundur
for i in range(6, 0, -1):
    print("hello")
    print(i)

for i in range(20):
    if i % 2 == 0:
        continue
    print(i)
