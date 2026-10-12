m = int(input())
jam = (m + 59) // 60
if jam == 1:
    biaya = 2000
else:
    biaya = 2000 + (jam - 1) * 1000
print(biaya)
