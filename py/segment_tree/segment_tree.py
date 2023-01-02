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


# recurisve
class ST:
    __slots__ = 'op', 'tree', 'n'
    def __init__(self, nums: list[int], op):
        self.op = op

        self.tree = [0] * len(nums) * 4
        self.n = len(nums)
        self._build(nums, 0, 0, len(nums) - 1)

    def _build(self, nums: list[int], tree_idx: int, l: int, r: int):
        if l == r:
            self.tree[tree_idx] = nums[l]
            return

        mid = (l + r) >> 1
        self._build(nums, (tree_idx << 1) + 1, l, mid)
        self._build(nums, (tree_idx << 1) + 2, mid + 1, r)

        self.tree[tree_idx] = self.op(
            self.tree[(tree_idx<<1) + 1],
            self.tree[(tree_idx<<1) + 2]
        )

    def query(self, l: int, r: int):
        return self._query(0, 0, self.n-1, l, r)

    def _query(self, tree_idx: int, seg_l: int, seg_r: int, l: int, r: int):
        # segment is fully inside the range
        if l <= seg_l and seg_r <= r:
            return self.tree[tree_idx]

        mid = (seg_l + seg_r) >> 1
        if l > mid:
            return self._query((tree_idx<<1)+2, mid+1, seg_r, l, r)
        elif r <= mid:
            return self._query((tree_idx<<1)+1, seg_l, mid, l, r)

        return self.op(
            self._query((tree_idx<<1)+1, seg_l, mid, l, mid),
            self._query((tree_idx<<1)+2, mid+1, seg_r, mid+1, r)
        )

    def update(self, idx: int, value: int):
        ...
        # self._update

    def _update(self, tree_idx: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.tree[tree_idx] = val
            return

        mid = (l+r) >> 1
        if idx > mid:
            self.udpate((tree_idx<<1) + 2, mid+1, r, idx, val)
        else:
            self.update((tree_idx<<1)+1, l, mid, idx, val)

        self.tree[tree_idx] = self.op(self.tree[(tree_idx<<1)+1], self.tree[(tree_idx<<1)+2])