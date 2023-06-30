def num(s, t):
    return "-" * t + "+" + "-" * (s - t - 1)


s = 10
t = 5
result = num(s, t)
print(result)
