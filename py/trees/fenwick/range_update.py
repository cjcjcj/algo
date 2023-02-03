"""
    1 - indexed

    Init: O(nlogn)
    Query: O(logn)
    Set: O(logn)
    Add: O(logn)
    Range-Add: O(logn)

    https://neerc.ifmo.ru/wiki/index.php?title=Дерево_Фенвика
    https://cp-algorithms.com/data_structures/fenwick.html
    https://programmingcontests.quora.com/Tutorial-Range-Updates-in-Fenwick-Tree
    https://kartikkukreja.wordpress.com/2013/12/02/range-updates-with-bit-fenwick-tree/comment-page-2/#comment-5442
"""

class Fenwick:
    def __init__(self, vals):
        n = len(vals)
        self.n = n+1
        self.tree = [0] * self.n
        for i, v in enumerate(vals):
            self.add(i, v)

    def _a(self, i: int, v):
        i += 1
        while i < self.n:
            self.tree[i] += v
            i += i & (-i)

    def add(self, i, v):
        self.range_add(i, i, v)

    def range_add(self, l, r, v):
        """[l, r]"""
        self._a(l, v)
        self._a(r + 1, -v)

    def get(self, i):
        s = 0
        i += 1
        while i:
            s += self.tree[i]
            i -= i & (-i)
        return s
