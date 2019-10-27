from typing import *


def repostaje(N: int, d: List[int]) -> List[int]:
    res = [0]
    km = N
    for i, gdist in enumerate(d):
        if gdist > km:
            res.append(i)
            km = N
        km -= gdist
    res.append(len(d))
    return res


print(repostaje(150, [130, 23, 45, 62, 12, 110, 130]))
