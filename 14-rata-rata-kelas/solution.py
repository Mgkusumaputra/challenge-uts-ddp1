def rata_rata(data):
    return sum(data) / len(data)

n = int(input())
data = list(map(int, input().split()))
print(f"{rata_rata(data):.2f}")
