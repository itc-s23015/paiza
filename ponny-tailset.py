def count_down(n):
    if n == 0:
        return "0!!"
    else:
        return str(n) + "\n" + count_down(n - 1)


n = int(input())
result = count_down(n)
print(result)
