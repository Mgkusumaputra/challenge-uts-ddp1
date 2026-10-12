n = int(input())
if n == 0:
    print("0")
else:
    bit = ""
    while n > 0:
        bit = str(n % 2) + bit
        n //= 2
    print(bit)
