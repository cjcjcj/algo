package segmenttree

type STR struct {
	n    int
	tree []int
	op   operation
}

func (st *STR) build(arr []int, treeIdx, l, r int) {
	if l == r {
		st.tree[treeIdx] = arr[l]
		return
	}

	mid := (l + r) >> 1
	st.build(arr, treeIdx<<1+1, l, mid)
	st.build(arr, treeIdx<<1+2, mid+1, r)

	st.tree[treeIdx] = st.op(st.tree[treeIdx<<1+1], st.tree[treeIdx<<1+2])
}

func NewSTR(nums []int, op operation) *STR {
	n := len(nums)
	tree := make([]int, n*4)
	st := &STR{
		n:    n,
		tree: tree,
		op:   op,
	}
	st.build(nums, 0, 0, n-1)
	return st
}

func (st *STR) query(treeIdx, segL, segR, l, r int) int {
	// inside range l...segL...segR...r
	if l <= segL && segR <= r {
		return st.tree[treeIdx]
	}

	mid := (segL + segR) >> 1
	if l > mid {
		// partial overlap {segL...[l...mid...segR}...r]
		// partial overlap [l....{segL...mid...r]...segR}
		// partial overlap {segL...[l....mid...r]...segR}
		return st.query(treeIdx<<1+2, mid+1, segR, l, r)
	} else if r <= mid {
		// partial overlap [l...{segL...r]...mid]...segR}
		// partial overlap {segL...[l...r]...mid]...segR}
		return st.query(treeIdx<<1+1, segL, mid, l, r)
	}

	// {segL...[l...mid...r]...segR}
	left := st.query(treeIdx<<1+1, segL, mid, l, mid)
	right := st.query(treeIdx<<1+2, mid+1, segR, mid+1, r)

	return st.op(left, right)
}

// Query performs operation query on [l; r] range
func (st *STR) Query(l, r int) int {
	return st.query(0, 0, st.n-1, l, r)
}

func (st *STR) update(treeIdx, l, r int, idx, val int) {
	if l == r {
		st.tree[treeIdx] = val
		return
	}

	mid := (l + r) >> 1
	if idx > mid {
		// l...mid...r...idx
		// l...mid...idx...r
		st.update(treeIdx<<1+2, mid+1, r, idx, val)
	} else {
		// l...idx...mid...r
		// idx...l...mid...r
		st.update(treeIdx<<1+1, l, mid, idx, val)
	}

	st.tree[treeIdx] = st.op(st.tree[treeIdx<<1+1], st.tree[treeIdx<<1+2])
}

// Update updates value of element w/ index idx
func (st *STR) Update(idx, value int) {
	st.update(0, 0, st.n-1, idx, value)
}

func (st *STR) Get(idx int) int {
	return 0
}
