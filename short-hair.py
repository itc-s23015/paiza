def f(N, S):
    idol = "\n".join([S] * N)
    return idol


N = int(input())
S = input()
result = f(N, S)
print(result)
