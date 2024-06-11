jawab = 'y'
friendList = []

while (jawab):
    nilai = input("Masukkan nama teman Anda: ")
    friendList.append(nilai)
    jawab = input("Tambahkan lagi? (y/n): ")

    if (jawab == 'n'):
        break

print("Daftar teman Anda: ", friendList)

print("=== Daftar teman Anda ===")
for i in friendList:
    print(i)

print("=== Jumlah index ===")
for i in range(len(friendList)):
    print((i + 1), " - ", friendList[i])


