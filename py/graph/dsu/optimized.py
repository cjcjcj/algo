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
