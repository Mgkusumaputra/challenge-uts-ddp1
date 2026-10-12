n = int(input())
tokens = input().split()
valid = 0
for token in tokens:
    try:
        int(token)
        valid += 1
    except ValueError:
        pass
print(valid)
