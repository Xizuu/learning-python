kalimat = input("Masukkan kalimat: ")
kalimat_list = list(kalimat)
print(kalimat_list)
print(len(kalimat_list))

jumlah_karakter = len(kalimat_list)
jumlah = 0
print(f"Kalimat dari {kalimat} memiliki {len(kalimat_list)} karakter")

for i in range(jumlah_karakter):
    jumlah += ord(kalimat_list[i])
    print(f'Karakter ke {i} adalah {kalimat_list[i]} dengan kode ASCII {ord(kalimat_list[i])}')

print(f'Jumlah hasil tambah kode ASCII untuk kalimat {kalimat} adalah {jumlah}')

