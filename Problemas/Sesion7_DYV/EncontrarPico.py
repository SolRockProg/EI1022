from typing import *


def top_finder(vector) -> Optional:
    indice1 = 0
    indice2 = len(vector)
    while not indice2 - indice1 == 1:
        half = (indice1 + indice2) // 2
        if vector[half] < vector[half - 1]:
            indice2 = half
        else:
            indice1 = half
    return vector[indice1]


if __name__ == "__main__":
    vector = [10,9, 8,7,6]
    print(top_finder(vector))
