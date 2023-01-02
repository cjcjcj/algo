package segmenttree

type STI struct {
	n    int
	tree []int
	op   operation
}

func NewSTI(nums []int, op operation) *STI {
	n := len(nums)

	tree := make([]int, n*2)
	for i := 0; i < n; i++ {
		tree[n+i] = nums[i]
	}
	for i := n - 1; i >= 0; i-- {
		tree[i] = op(tree[i<<1], tree[(i<<1)|1])
	}

	return &STI{
		n:    len(nums),
		tree: tree,
		op:   op,
	}
}

// Query performs operation query on [l; r] range
func (st *STI) Query(l, r int) int {
	res := 0
	l += st.n
	r += st.n

	for ; l < r; l, r = l>>1, r>>1 {
		if l&1 == 1 {
			res = st.op(res, st.tree[l])
			l += 1
		}
		if r&1 == 0 {
			res = st.op(res, st.tree[r])
			r -= 1
		}
	}
	return res
}

// Update updates value of element w/ index idx
func (st *STI) Update(idx, value int) {
	idx += st.n
	st.tree[idx] = value
	for ; idx > 1; idx >>= 1 {
		st.tree[idx>>1] = st.op(st.tree[idx], st.tree[idx^1])
	}
}

func (st *STI) Get(idx int) int {
	return st.tree[st.n+idx]
}
