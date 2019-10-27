def activities_optimizer(C: set):
    activities = sorted(C, key=lambda t: t[1])
    res = []
    t1 = min(s for s, t in C)
    for s, t in activities:
        if t1 <= s:
            res.append((s, t))
            t1 = t
    return res


x = {(1, 5), (1, 2), (3, 6), (4, 7), (6, 7)}
print(activities_optimizer(x))
