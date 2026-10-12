s = input().strip()
k = int(input())
k %= len(s)
print(s[k:] + s[:k])
