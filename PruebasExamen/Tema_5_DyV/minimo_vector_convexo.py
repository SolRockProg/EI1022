def min_v_convexo(vector):
    def rec(vector, b, e):
        if e - b == 1:
            return vector[b]
        elif e - b == 2:
            return min(vector[b], vector[b + 1])
        else:
            half = (e + b) // 2
            if vector[half] >= vector[half - 1]:
                return rec(vector, b, half)
            else:
                return rec(vector, half, e)

    return rec(vector, 0, len(vector))
