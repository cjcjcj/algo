"""
    https://codeforces.com/blog/entry/18051
    https://brestprog.by/topics/segmenttree/
    https://e-maxx.ru/algo/segment_tree


    S: O(2n)
    T:
        init O(n)
        q    O(logn)
        add  O(logn)
"""


class ST:
    __slots__ = 'op', 'tree', 'n'
    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = nums * 2
        for i in reversed(range(self.n)):
            self.tree[i] = self.tree[2*i] + self.tree[2*i + 1]

    def query(self, l: int, r: int) -> int:
        l, r = l+self.n, r+self.n
        res = 0
        while l <= r:
            if l%2 == 1:
                res += self.tree[l]
                l += 1
            if r%2 == 0:
                res += self.tree[r]
                r -= 1
            l, r = l//2, r//2
        return res

    def update(self, k: int, value: int):
        k += self.n
        self.tree[k] = value
        k //= 2
        while k >= 1:
            self.tree[k] = self.tree[2*k] + self.tree[2*k+1]
            k //= 2
