from classes import Student
import bisect


class BTreeNode:

    def __init__(self, leaf=False, degree: int = 3):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.degree = degree
        # self.max_keys = depth * 2 - 1
        # self.max_children = depth * 2

    def set_leaf(self, leaf: bool) -> None:
        self.leaf = leaf

    def insert_key(self, key: Student) -> None:
        if self.leaf:
            bisect.insort(self.keys, key, key=lambda x: x.num_id)

        if not self.has_available_space():
            self.split_child()
            self.set_leaf(False)
            return

        if key.get_id() > self.keys[-1].get_id():
            self.children[-1].insert_key(key)
            return

        if key.get_id() < self.keys[0].get_id():
            self.children[0].insert_key(key)
            return

    def split_child(self) -> Student:
        print(f'Splitting on keys: {self.keys}')
        left_child = BTreeNode(leaf=True, degree=self.degree)
        right_child = BTreeNode(leaf=True, degree=self.degree)
        middle_index = len(self.keys) // 2

        for i in range(0, middle_index):
            left_child.insert_key(self.keys.pop(0))

        self.add_child(left_child)

        for i in range(len(self.keys) - 1):
            right_child.insert_key(self.keys.pop(-1))

        self.add_child(right_child)

    def add_child(self, child: Student) -> None:
        self.children.append(child)

    def is_leaf(self) -> bool:
        return self.leaf

    def get_keys(self) -> list:
        return self.keys

    def get_child(self, index: int) -> Student:
        return self.children[index]

    def get_children(self) -> [Student]:
        return self.children

    def get_number_of_children(self) -> int:
        return sum(x is not None for x in self.children)

    def get_number_of_keys(self) -> int:
        return len(self.keys)

    def has_available_space(self) -> bool:
        return len(self.keys) < (2 * self.degree - 1)

    def __str__(self) -> str:
        return str()
