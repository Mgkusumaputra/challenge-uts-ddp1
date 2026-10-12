def harga_akhir(total):
    if total >= 100000:
        return total * 90 // 100
    return total

total = int(input())
print(harga_akhir(total))
