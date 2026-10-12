n = int(input())
nilai = list(map(int, input().split()))
jumlah = [0, 0, 0, 0, 0]
for x in nilai:
    if x >= 85: jumlah[0] += 1
    elif x >= 70: jumlah[1] += 1
    elif x >= 55: jumlah[2] += 1
    elif x >= 40: jumlah[3] += 1
    else: jumlah[4] += 1
print(*jumlah)
