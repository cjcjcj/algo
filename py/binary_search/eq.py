def bs(arr: list[int], target: int):
    l, r = 0, len(arr)

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return -1
