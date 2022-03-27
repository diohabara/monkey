# path compress and union by rank
class UnionFind:
    def __init__(self, n: int) -> None:
        """
        Time: O(N)
        Space: O(N)
        """
        self.parent = [-1] * n  # parent, if not set, then -1
        self.rank = [1] * n  # how big the group is

    # return x's group, and compress the path
    def root(self, x: int) -> int:
        """
        Time: O(α(N))
        Space: O(1)
        """
        if self.parent[x] == -1:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    # check if x and y are in the same group
    def is_connected(self, x: int, y: int) -> bool:
        """
        Time: O(α(N))
        Space: O(1)
        """
        return self.root(x) == self.root(y)

    # unite x's group and y's group
    def unite(self, x: int, y: int) -> bool:
        """
        Time: O(α(N))
        Space: O(1)
        """
        root_x = self.root(x)
        root_y = self.root(y)
        # already connected
        if root_x == root_y:
            return False
        # union by rank(y should be smaller)
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        return True


def test_disjoint_set() -> None:
    uf = UnionFind(7)
    uf.unite(1, 2)
    uf.unite(2, 3)
    uf.unite(5, 6)
    assert uf.is_connected(1, 3)
    assert not uf.is_connected(2, 5)
    uf.unite(1, 6)
    assert uf.is_connected(2, 5)
