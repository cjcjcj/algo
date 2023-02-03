"""
    0 - indexed

    Init: O(nlogn)
    Query: O(logn)
    Set: O(logn)
    Add: O(logn)

    https://neerc.ifmo.ru/wiki/index.php?title=Дерево_Фенвика
    https://cp-algorithms.com/data_structures/fenwick.html
"""


class Fenwick:
    def __init__(self, vals):
        n = len(vals)
        self.tree = [0]*n
        for i in range(n):
            self.add(i, vals[i])

    def _q(self, l):
        s = 0
        while l >= 0:
            s += self.tree[l]
            l = (l & (l+1)) - 1
        return s

    def query(self, l, r):
        """[l, r]"""
        return self._q(r) - self._q(l-1)

    def add(self, i, v):
        while i < len(self.tree):
            self.tree[i] += v
            i = i | (i+1)

    def get(self, i):
        return self.query(i, i)

    def set(self, i, v):
        self.add(i, v - self.get(i))
