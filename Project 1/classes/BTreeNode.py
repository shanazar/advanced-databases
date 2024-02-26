
class BTreeNode:

    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

    def set_leaf(self, leaf: bool) -> None:
        self.leaf = leaf

    def add_key(self, key: str) -> None:
        self.keys.append(key)

    def add_child(self, child) -> None:
        self.child.append(child)

    def is_leaf(self) -> bool:
        return self.leaf

    def get_keys(self) -> list:
        return self.keys

    def get_child(self, index: int):
        return self.child[index]
    