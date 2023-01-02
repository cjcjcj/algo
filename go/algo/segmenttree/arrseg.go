package segmenttree

type ArrSeg []struct {
	op        operation
	l, r, val int
}

func (t ArrSeg) Build(treeIdx, l, r int, nums []int, op operation) {
	t[treeIdx].op = op

	t[treeIdx].l, t[treeIdx].r = l, r
	if l == r {
		t[treeIdx].val = nums[l]
		return
	}

	mid := (l + r) >> 1
	t.Build(treeIdx<<1+1, l, mid, nums, op)
	t.Build(treeIdx<<1+2, mid+1, r, nums, op)

	t[treeIdx].val = t[treeIdx].op(t[treeIdx<<1+1].val, t[treeIdx<<1+2].val)
}

func (t ArrSeg) Update(treeIdx, idx, val int) {
	if t[treeIdx].l == t[treeIdx].r {
		t[treeIdx].val = val
		return
	}
	mid := (t[treeIdx].l + t[treeIdx].r) >> 1
	if idx <= mid {
		t.Update(treeIdx<<1+1, idx, val)
	} else {
		t.Update(treeIdx<<1+2, idx, val)
	}
	t[treeIdx].val = t[treeIdx].op(t[treeIdx<<1+1].val, t[treeIdx<<1+2].val)
}

func (t ArrSeg) Query(treeIdx, l, r int) int {
	if l <= t[treeIdx].l && t[treeIdx].r <= r {
		return t[treeIdx].val
	}

	mid := (t[treeIdx].l + t[treeIdx].r) >> 1
	if l > mid {
		return t.Query(treeIdx<<1+2, l, r)
	} else if r <= mid {
		return t.Query(treeIdx<<1+1, l, r)
	}

	return t[treeIdx].op(
		t.Query(treeIdx<<1+1, l, mid),
		t.Query(treeIdx<<1+2, mid+1, r),
	)
}

func (t ArrSeg) Get(treeIdx, r int) int {
	// if t[treeIdx].l == t[treeIdx].r {
	// 	return t[treeIdx].l
	// }
	// mid := (t[treeIdx].l + t[treeIdx].r) >> 1
	// if mid < r {
	// 	return t.index(treeIdx<<1+2, r)
	// }
	return 0
}

func NewCHSeg(nums []int, op operation) ArrSeg {
	t := make(ArrSeg, len(nums)*4)
	t.Build(0, 0, len(nums)-1, nums, op)
	return t
}
