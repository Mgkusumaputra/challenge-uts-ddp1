def parse_log(baris):
    nama, status, durasi = baris.split()
    return status, int(durasi)

n = int(input())
jumlah_ok = 0
total_durasi = 0
for _ in range(n):
    status, durasi = parse_log(input())
    if status == "OK":
        jumlah_ok += 1
        total_durasi += durasi
print(jumlah_ok, total_durasi)
