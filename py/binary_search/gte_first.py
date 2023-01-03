def bs(arr: list[int], target: int):
    l, r = 0, len(arr) - 1
    result = -1

    while l <= r:
        mid = (l + r) >> 1
        if arr[mid] >= target:
            result = mid
            r = mid - 1
        else:
            l = mid + 1

    return result
