"""
    https://codeforces.com/blog/entry/18051
    https://brestprog.by/topics/segmenttree/
    https://e-maxx.ru/algo/segment_tree
"""


# import operator
# ops = (
#     min,
#     max,
#     operator.add,
# )


class ST:
    __slots__ = 'op', 'tree', 'n'
    def __init__(self, nums: list[int], op):
        self.op = op

        self.n = len(nums)
        self.tree = nums * 2
        for i in reversed(range(self.n)):
            self.tree[i] = op(self.tree[i<<1], self.tree[i<<1 | 1])

    def query(self, l: int, r: int) -> int:
        op = self.op

        res = 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = op(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = op(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def update(self, idx: int, value: int):
        # idx = 2*i     ->  idx^1 = 2*i + 1
        # idx = 2*i + 1 ->  idx^1 = 2*i
        op = self.op

        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            self.tree[idx >> 1] = op(self.tree[idx], self.tree[idx^1])
            idx >>= 1
