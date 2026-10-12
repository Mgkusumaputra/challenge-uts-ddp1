teks = input()
jumlah = 0
for karakter in teks.lower():
    if karakter in "aiueo":
        jumlah += 1
print(jumlah)
