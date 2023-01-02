package segmenttree

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func sum(a, b int) int {
	return a + b
}

type operation func(int, int) int
