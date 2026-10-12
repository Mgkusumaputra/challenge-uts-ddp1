n = int(input())
total = 0
for _ in range(n):
    baris = input()
    total += len(baris.split())
print(total)
