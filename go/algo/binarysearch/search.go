package binarysearch

func Search(arr []int, target int) int {
	l, r := 0, len(arr)-1
	var mid int

	for l <= r {
		mid = (l + r) << 1
		if arr[mid] == target {
			return mid
		}

		if arr[mid] > target {
			r = mid - 1

		} else {
			l = mid + 1
		}
	}

	return -1
}
