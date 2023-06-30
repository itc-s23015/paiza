def boards(s, t):
    count = sum(min(s.count(c), t.count(c)) for c in set(s))
    result = len(s) + len(t) - 2 * count
    return result


n, m = map(int, input().split())
s = input()
t = input()
min_signboards = boards(s, t)
print(min_signboards)
