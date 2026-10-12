n = int(input())
suhu = list(map(int, input().split()))
jumlah = 0
for x in suhu:
    if x < 18 or x > 30:
        jumlah += 1
print(jumlah)
