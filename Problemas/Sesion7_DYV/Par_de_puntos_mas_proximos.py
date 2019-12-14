import math
from typing import *


def d(a: Tuple[float], b: Tuple[float]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def puntos_prox(z: List[Tuple[float]], b: int, e: int) -> Tuple[Optional[Tuple[float]], Optional[Tuple[float]], float]:
    if e - b <= 1:
        return (None, None, float("infinity"))
    if e - b == 2:
        return (z[0], z[1], d(z[0], z[1]))
    else:
        splitter = (b + e) // 2
        left = puntos_prox(z, b, splitter)
        right = puntos_prox(z, splitter, e)
        delta = min(left[2], right[2])
        for left_point in


if __name__ == "__main__":
    z = [(0.5, 3.5), (1, 2), (3, 2), (3.5, 1.5), (4, 3.5), (5, 0.5), (5, 3), (5.5, 1.5)]
    z = sorted(z, key=lambda x: x[0])
