def points(p):


normal = p // 100
bonus = 10 if p >= 1000 else 0
return normal + bonus

p = int(input())
result = points(p)
print(result)
