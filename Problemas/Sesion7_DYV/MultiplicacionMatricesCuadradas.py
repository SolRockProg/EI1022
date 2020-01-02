class SqMatrix:
    def __init__(self, A: "square matrix" = None, n: "int" = 0):
        if A != None:
            if any(len(A) != len(row) for row in A): raise Exception("Non square matrix")
            self.n, self.A = len(A), A
        else:
            self.n, self.A = n, [[0] * n for _ in range(n)]

    def __getitem__(self, ij: "(int, int)"):
        return self.A[ij[0]][ij[1]]

    def __setitem__(self, ij: "(int, int)", value: "T"):
        self.A[ij[0]][ij[1]] = value
        return value

    def __add__(self, other: "SqMatrix"):
        if other.n != self.n: raise Exception("Different size matrices.")
        r = SqMatrix([[self[i, j] + other[i, j] for j in range(self.n)] for i in range(self.n)])
        return r

    def __sub__(self, other: "SqMatrix"):
        if other.n != self.n: raise Exception("Different size matrices.")
        r = SqMatrix([[self[i, j] - other[i, j] for j in range(self.n)] for i in range(self.n)])
        return r

    def split(self):
        mid = self.n // 2
        a = SqMatrix([[self[i, j] for j in range(mid)] for i in range(mid)])
        b = SqMatrix([[self[i, j] for j in range(mid, self.n)] for i in range(mid)])
        c = SqMatrix([[self[i, j] for j in range(mid)] for i in range(mid, self.n)])
        d = SqMatrix([[self[i, j] for j in range(mid, self.n)] for i in range(mid, self.n)])
        return a, b, c, d

    def join(self, a: "SqMatrix", b: "SqMatrix", c: "SqMatrix", d: "SqMatrix"):
        mid = self.n // 2
        for i in range(mid):
            for j in range(mid): self[i, j] = a[i, j]
            for j in range(mid, self.n): self[i, j] = b[i, j - mid]
        for i in range(mid, self.n):
            for j in range(mid): self[i, j] = c[i - mid, j]
            for j in range(mid, self.n): self[i, j] = d[i - mid, j - mid]

    def __mul__(self, other: "SqMatrix"):
        if other.n != self.n: raise Exception("Different size matrices.")
        if self.n == 1: return SqMatrix([[self[0, 0] * other[0, 0]]])
        a, b, c, d = self.split()
        e, f, g, h = other.split()
        P1, P2, P3, P4 = a * (f - h), (a + b) * h, (c + d) * e, d * (g - e)
        P5, P6, P7 = (a + d) * (e + h), (b - d) * (g + h), (a - c) * (e + f)
        r = P5 + P4 - P2 + P6
        s = P1 + P2
        t = P3 + P4
        u = P5 + P1 - P3 - P7
        result = SqMatrix(n=self.n)
        result.join(r, s, t, u)
        return result
