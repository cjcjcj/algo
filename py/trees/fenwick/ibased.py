"""
    1 - indexed

    Init: O(nlogn)
    Query: O(logn)
    Set: O(logn)
    Add: O(logn)

    https://neerc.ifmo.ru/wiki/index.php?title=Дерево_Фенвика
    https://cp-algorithms.com/data_structures/fenwick.html
"""


class Fenwick:
    def __init__(self, vals):
        self.n = len(vals)+1
        self.tree = [0]*self.n
        for i, v in enumerate(vals):
            self.add(i, v)
    def _q(self, l):
        s = 0
        l += 1
        while l > 0:
            s += self.tree[l]
            l -= l & (-l)
        return s
    def query(self, l, r):
        """[l, r]"""
        return self._q(r) - self._q(l-1)
    def add(self, i, v):
        i += 1
        while i < self.n:
            self.tree[i] += v
            i += i & (-i)
    def get(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def set(self, i, v):
        self.add(i, v - self.get(i))
