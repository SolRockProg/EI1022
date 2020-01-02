def quicksort_basico(vector):
    if len(vector) <= 1:
        return vector
    else:
        pivot = vector[0]
        vector_der = [elem for elem in vector if elem > pivot]
        vector_izq = [elem for elem in vector[1:] if elem <= pivot]
        return quicksort_basico(vector_izq) + [pivot] + quicksort_basico(vector_der)


def quicksort_indexes(vector):
    def partition(b, e) -> int:
        pivot = vector[e - 1]
        i = b - 1
        for j in range(b, e-1):
            if vector[j] <= pivot:
                i += 1
                vector[i], vector[j] = vector[j], vector[i]
        vector[i + 1], vector[e - 1] = vector[e - 1], vector[i + 1]
        return i + 1

    def rec(b, e):
        if e - b > 1:
            pivot = partition(b, e)
            rec(b, pivot)
            rec(pivot + 1, e)

    rec(0, len(vector))

if __name__=="__main__":
    array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
    quicksort_indexes(array)
    print(array)