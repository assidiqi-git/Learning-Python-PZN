kata = input("kata :")
huruf_dicari = input("huruf dicari :")

for huruf in kata:
    if huruf == huruf_dicari:
        print(f"Huruf {huruf} ditemukan")
        break
else:
    print(f"Huruf {huruf_dicari} tidak ditemukan")
