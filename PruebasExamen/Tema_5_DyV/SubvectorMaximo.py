def max_suma(v):
    def select_sum(left, right, half):
        left_b, left_e, sum_left = left
        right_b, right_e, sum_right = right
        sumador = 0
        index_left = 0
        acum_left = 0
        for i in range(half - 1, left_b - 1, -1):
            sumador += v[i]
            acum_left, index_left = max((acum_left, index_left), (sumador, i))
        sumador = 0
        index_right = 0
        acum_right = 0
        for i in range(half, right_e):
            sumador += v[i]
            acum_right, index_right = max((acum_right, index_right), (sumador, i))
        best = max(sum_left, sum_right, acum_left + acum_right)
        if best == sum_left:
            return left_b, left_e, sum_left
        elif best == sum_right:
            return right_b, right_e, sum_right
        else:
            return index_left, index_right + 1, best

    def divide(b, e):
        if e - b == 1:
            return b, e, v[b]
        half = (b + e) // 2
        return select_sum(divide(b, half), divide(half, e), half)

    return divide(0, len(v))


if __name__ == "__main__":
    vector = [10, 0]
    b, e, a = max_suma(vector)
    print("El maximo subvector encontrado es: ")
    print(vector[b:e])
    print("con un valor de: " + str(a))
