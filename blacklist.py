blacklistedWords = []

with open('blacklist.txt', 'r') as file:
    blacklistedWords = [line.strip() for line in file]

kalimat = input('Masukkan kalimat: ');

for word in blacklistedWords:
    if word in kalimat:
        if len(word) > 3:
            kalimat = kalimat.replace(word, word[:-3] + '***')
        else:
            kalimat = kalimat.replace(word, '*' * len(word))

print(kalimat)