# https://codeforces.com/blog/entry/18051
# https://brestprog.by/topics/segmenttree/
# https://e-maxx.ru/algo/segment_tree

# import operator
# ops = (
#     min,
#     max,
#     operator.add,
# )


# iterative
class ST:
    __slots__ = 'op', 'tree', 'n'
    def __init__(self, nums: list[int], op):
        self.op = op

        self.n = len(nums)
        self.tree = nums * 2
        for i in range(self.n - 1, 0, -1):
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


# recurisve
class ST:
    __slots__ = 'op', 'tree', 'n'
    def __init__(self, nums: list[int], op):
        self.op = op

        self.tree = nums * 4
        self.n = len(nums)
        self._build(nums, 1, 0, len(nums) - 1)

    def _build(self, nums: list[int], v: int, tl: int, tr: int):
        if tl == tr:
            self.tree[v] = nums[tl]
        else:
            tm = (tl + tr) >> 1
            self._build(nums, v << 1, tl, tm)
            self._build(nums, (v << 1) + 1, tm + 1, tr)
            self.tree[v] = self.op(self.tree[v<<1], self.tree[(v<<1) + 1])

    def query(self, l: int, r: int, v: int = 1, tl: int = 0, tr: int = -1):
        if tr == -1: tr = self.n - 1
        if l > r:
            return 0
        if l == tr and r == tr:
            return self.tree[v]
        tm = (tl + tr) >> 1
        return self.op(
            self.query(l, min(r, tm), v << 1, tl, tm),
            self.query(max(l, tm+1), r, (v << 1) + 1, tm+1, tr)
        )

    def update(self, pos: int, new: int, v: int = 1, tl: int = 0, tr: int = -1):
        if tr == -1: tr = self.n - 1
        if tl == tr:
            self.tree[v] = new
        else:
            tm = (tl + tr) >> 1
            if pos <= tm:
                self.update(pos, new, v << 1, tl, tm)
            else:
                self.update(pos, new, (v << 1) + 1, tm+1, tr)
            self.tree[v] = self.op(self.tree[v<<1], self.tree[(v<<1) + 1])
