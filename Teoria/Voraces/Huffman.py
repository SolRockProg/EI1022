from algoritmia.datastructures.priorityqueues import MinHeap


def build_tree(freq):
    T = MinHeap([[(freq[symbol], symbol)] for symbol in freq])
    while len(T) > 1:
        left_tree = T.extract_opt()
        right_tree = T.extract_opt()
        T.add([(left_tree[0][0] + right_tree[0][0],), left_tree, right_tree])
    return T


e = {"a": 30, "b": 25, "c": 15, "d": 20, "e": 10}
print(build_tree(e))
