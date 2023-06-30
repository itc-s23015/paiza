def eye(d, e):
    eye = [(d, e) for _ in range(5)]
    return "OK" if sum(d == e for d, e in eye) >= 3 else "NG"


d, e = input().split()
result = eye(d, e)
print(result)
