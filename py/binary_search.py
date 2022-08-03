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


def bs_first(arr: list[int], target: int):
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
            r = mid -1

    return result


def bs_first_closest_gte(arr: list[int], target: int):
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


def bs_last(arr: list[int], target: int):
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
