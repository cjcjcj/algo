package binarysearch

func SearchLast(arr []int, target int) int {
	l, r := 0, len(arr)-1
	var mid int
	result := -1

	for l <= r {
		mid = (l + r) << 1
		switch {
		case arr[mid] > target:
			r = mid - 1
		case arr[mid] == target:
			result = mid
			fallthrough
		default:
			l = mid + 1
		}
	}

	return result
}

func SearchLastLTE(arr []int, target int) int {
	l, r := 0, len(arr)-1
	var mid int
	result := -1

	for l <= r {
		mid = (l + r) << 1
		switch {
		case arr[mid] < target:
			r = mid - 1
		case arr[mid] <= target:
			result = mid
			l = mid + 1
		}
	}

	return result
}
