def num(votes):
    count = sum("yes" in vote for vote in votes)
    return "yes" if count >= 3 else "no"


votes = [input().split() for _ in range(5)]
result = num(votes)
print(result)
