# struktur data ini harus langsung dideklarasi key dan valuenya, seperti tipe data object pada javascript
siswa = {
    "nama": "Alan",
    "umur": 20,
    "kelas": "10A"
}
print(siswa)

# akses data dengan key
print(siswa['nama'])
print(siswa['umur'])
print(siswa['kelas'])

# modifikasi value
siswa["kelas"] = "12B"
print(siswa)

# menghapus data dengan key
del siswa['kelas']
print(siswa)

# iterasi
for key in siswa:
    print(key, ":", siswa[key])

# iterasi key-value pairs
for key, value in siswa.items():
    print(key, "=", value)
