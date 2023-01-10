"""
    Init: O(nlogn)
    Query: O(logn)
    Set: O(logn)
    Add: O(logn)

    https://neerc.ifmo.ru/wiki/index.php?title=Дерево_Фенвика
"""


class Fenwick:
    def __init__(self, vals):
        n = len(vals)
        self.tree = [0]*n
        for i in range(n):
            j = i
            while j < n:
                self.tree[j] += vals[i]
                j |= j+1

    def _q(self, l):
        s = 0
        while l >= 0:
            s += self.tree[l]
            l &= l+1
            l -= 1
        return s

    def query(self, l, r):
        """[l, r]"""
        return self._q(r) - self._q(l-1)

    def add(self, i, v):
        while i < len(self.tree):
            self.tree[i] += v
            i |= i+1

    def get(self, i):
        return self.query(i, i)

    def set(self, i, v):
        self.add(i, v - self.get(i))
