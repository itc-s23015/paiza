def ame(m, n):
    return "ok" if m % n == 0 else "ng"


n, m = map(int, input().split())
result = ame(m, n)
print(result)
