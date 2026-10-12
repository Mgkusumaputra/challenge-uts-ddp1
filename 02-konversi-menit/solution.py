s = int(input())
jam = s // 3600
sisa = s % 3600
menit = sisa // 60
detik = sisa % 60
print(jam, menit, detik)
