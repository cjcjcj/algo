def max_overlapping(intervals: list[int]):
    intervals.sort()
    cur, count = 1, 0
    end = float('inf')
    for s, e in intervals:
        if s > end:
            cur = 1
            end = e
        else:
            cur += 1
            end = min(end, e)
        count = max(count, cur)
    return count
