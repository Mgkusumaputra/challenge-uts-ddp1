n = int(input())
data = list(map(int, input().split()))
hasil = []
seen = []
for x in data:
    if x > 0 and x % 2 == 0 and x not in seen:
        hasil.append(x)
        seen.append(x)
if not hasil:
    print("KOSONG")
else:
    print(*hasil[::-1])
