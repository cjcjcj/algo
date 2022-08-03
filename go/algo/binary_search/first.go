package binarysearch

func SearchFirst(arr []int, target int) int {
	l, r := 0, len(arr)-1
	var mid int
	result := -1

	for l <= r {
		mid = (l + r) << 1
		switch {
		case arr[mid] < target:
			l = mid + 1
		case arr[mid] == target:
			result = mid
			fallthrough
		default:
			r = mid - 1
		}
	}

	return result
}

func SearchFirstGTE(arr []int, target int) int {
	l, r := 0, len(arr)-1
	var mid int
	result := -1

	for l <= r {
		mid = (l + r) << 1
		switch {
		case arr[mid] < target:
			l = mid + 1
		case arr[mid] >= target:
			result = mid
			r = mid - 1
		}
	}

	return result
}
