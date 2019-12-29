def binpacking(W, C):
    indexes = sorted(range(len(W)), key=lambda x: -W[x])
    containers = [C]
    res = [0] * len(W)
    for index in indexes:
        for i, c in enumerate(containers):
            if c >= W[index]:
                containers[c] -= W[index]
                res[index] = i
                break
        else:
            res[index] = len(containers)
            containers.append(C - W[index])
    return res
