# SC: O(V)
# TC: init - O(V), find/union/connectivity O(Accerman(V))
class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.h = [1] * n

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.h[root_x] > self.h[root_y]:
            self.root[root_y] = root_x
        elif self.h[root_x] < self.h[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x
            self.h[root_x] += 1

    def find(self, x):
        if self.root[x] == x:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
