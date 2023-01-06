"""
    supports range updates
    T:
        init    O(n)
        q       O(n)
        upd     O(1)
"""


class DA:
    def __init__(self, ns: int):
        self.l = ns.copy()
        for i in range(1, len(ns)):
            self.l[i] -= ns[i-1]

    def q(self, i: int) -> int:
        return sum(self.l[:i+1])

    def update(self, l: int, r: int, v: int):
        self.l[l] += v
        self.l[r+1] -= v
