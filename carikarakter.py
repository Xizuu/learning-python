kalimat = input("Masukkan kalimat: ")
cari = input("Karakter yang ingin dicari: ")
kalimat_list = list(kalimat)
jumlah_karakter = len(kalimat)

for i in range(jumlah_karakter):
    if cari in kalimat_list[i]:
        print(f"Karakter {cari} ditemukan pada indeks {i}")
        break
    else:
        print(f"Karakter {cari} tidak ditemukan pada indeks {i}")
