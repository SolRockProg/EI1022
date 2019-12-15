from algoritmia.datastructures.lists import IList


class MedianOf5Selector(object):
    def __init__(self, threshold: "int" = 10):
        self.threshold = threshold

    def median_of_5(self, a, i) -> "T":
        u, v, w, x = a[i], a[i + 1], a[i + 2], a[i + 3]
        if v > u:
            u, v = v, u
        if x > w:
            w, x = x, w
        if u < w:
            u = a[i + 4]
        if v > u:
            u, v = v, u
        else:
            w = a[i + 4]
        if w > x:
            w, x = x, w
        if u < w:
            return v if v < w else w
        else:
            return x if x < u else u

    def select(self, a, k):
        if not 0 <= k < len(a):
            raise IndexError(repr(k))
        if len(a) < self.threshold:
            return sorted(a)[k]
        else:
            groups = len(a)//5
            pivot = self.select([self.median_of_5(a, (len(a) // groups) * i) for i in range(0, groups)],
                                groups // 2)
            lessthan, equal = 0, 0
            for v in a:
                if v < pivot:
                    lessthan += 1
                elif v == pivot:
                    equal += 1
            if k < lessthan:
                return self.select([v for v in a if v < pivot], k)
            elif k >= lessthan + equal:
                return self.select([v for v in a if v > pivot], k - lessthan - equal)
            else:
                return pivot

if __name__=="__main__":
    v = [1, 6, 8, 56, 12, 9, 48, 0, 23, 40, 2, 31, 23, 7, 87, 18]
    print('Ordenado :', sorted(v))
    print('Con select:', [MedianOf5Selector().select(v[:], i) for i in range(len(v))])
