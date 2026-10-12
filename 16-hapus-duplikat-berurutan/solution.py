data = list(map(int, input().split()))
hasil = []
for x in data:
    if not hasil or hasil[-1] != x:
        hasil.append(x)
print(*hasil)
