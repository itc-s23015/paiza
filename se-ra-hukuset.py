def str(n):
    return "_".join(n)


n = int(input())
word = [input() for _ in range(n)]
result = str(word)
print(result)
