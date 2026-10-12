n = int(input())
angka = []
while len(angka) < n:
    angka.extend(map(int, input().split()))
for x in angka[:n]:
    print("GENAP" if x % 2 == 0 else "GANJIL")
