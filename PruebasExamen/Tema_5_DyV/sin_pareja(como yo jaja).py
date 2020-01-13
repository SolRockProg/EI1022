def sin_pareja(v, i, j):
    if j - i == 1:
        return i
    else:
        half = (i + j) // 2
        if v[half - 1] is not v[half] and v[half + 1] is not v[half]:
            return half
        elif (v[half - 1] == v[half] and half % 2 == 0) or (v[half + 1] == v[half] and half % 2 != 0):
            return sin_pareja(v, i, half)
        else:
            return sin_pareja(v, half, j)


if __name__ == "__main__":
    v = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
    pos = sin_pareja(v, 0, len(v))
    print(pos, v[pos])