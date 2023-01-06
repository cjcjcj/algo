def merge(intervals: list[int]):
    intervals.sort()
    start, end = intervals[0]
    r = []
    for s, e in intervals:
        if s > end:
            r.append((start, end))
            end = e
            start = s
        else:
            end = max(end, e)
    r.append((start,end))
    return r
