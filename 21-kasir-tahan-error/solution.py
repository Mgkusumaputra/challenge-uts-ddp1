n = int(input())
tokens = input().split()
total = 0
for token in tokens:
    try:
        harga = int(token)
        if harga >= 0:
            total += harga
    except ValueError:
        continue
print(total)
