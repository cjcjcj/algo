"""
    :9 quick union + path shortening + union by rank
    :65 quick find
    :
"""
from logging import root


# SC: O(V)
# TC: init - O(V), find/union/connectivity O(Accerman(V))
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.h = [1] * n

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.h[root_x] == self.h[root_y]:
            self.parent[root_y] = root_x
            self.h[root_x] += 1
        elif self.h[root_x] < self.h[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


# SC: O(V)
# TC: init - O(V), find/connectivity O(1), union O(V)
class DSU:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return

        for i in range(len(self.root)):
            if self.root[i] == root_y:
                self.root[i] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

