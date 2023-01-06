from collections import deque


def sliding_min(ns: list[int], k: int):
    q = deque()

    for i, n in enumerate(ns):
        while q and q[0][-1] <= i-k:
            q.popleft()
        while q and q[-1][0] > n:
            q.pop()
        q.append((n, i))
