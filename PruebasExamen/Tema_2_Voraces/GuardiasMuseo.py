from typing import *


def guardias_museo(X: List[float], D: float) -> List[float]:
    guardias = []
    for i, cuadro in enumerate(X):
        if i == 0:
            guardias.append(cuadro + D)
        elif cuadro - guardias[-1] > D:
            guardias.append(cuadro + D)
    return guardias


if __name__ == "__main__":
    D = 2.5
    X = [3, 5, 6.4, 7.8, 10.1, 20.2]
    print(guardias_museo(X, D))
