n = int(input())
harga = list(map(int, input().split()))
total = 0
for h in harga:
    total += h
print(total)
