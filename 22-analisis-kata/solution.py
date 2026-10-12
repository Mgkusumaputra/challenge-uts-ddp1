import string
kalimat = input().lower()
for tanda in ".,!?;:":
    kalimat = kalimat.replace(tanda, " ")
kata = kalimat.split()
terpanjang = kata[0]
for x in kata[1:]:
    if len(x) > len(terpanjang):
        terpanjang = x
print(terpanjang)
