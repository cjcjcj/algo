def bs(arr: list[int], target: int):
    l, r = 0, len(arr)
    result = -1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] > target:
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            result = mid
            l = mid + 1

    return result
