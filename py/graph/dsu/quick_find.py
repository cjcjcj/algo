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

