def repetido_vector(v):
    if len(v) == 2:
        return v[0]
    half = len(v) // 2
    if v[half] == v[half + 1] or v[half] == v[half - 1]:
        return v[half]
    elif half >= v[half]:
        return repetido_vector(v[:half])
    else:
        return repetido_vector(v[half:])


if __name__ == "__main__":
    v = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(repetido_vector(v))
