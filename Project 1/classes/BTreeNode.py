from typing import Tuple, Any

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
        bisect.insort(self.keys, key, key=lambda x: x.num_id)

    def split_node(self, value: Student = None, leaf: bool = True):
        if value:
            self.insert_key(value)
            extracted_key = self.keys.pop((len(self.keys) // 2) - 1)
        else:
            extracted_key = self.keys.pop((len(self.keys) // 2))
        new_node = BTreeNode(leaf=leaf, degree=self.degree)
        for i in range(len(self.keys) // 2):
            new_node.insert_key(self.keys.pop(0))
        for i in range(len(self.children) // 2):
            new_node.add_child(self.children.pop(0))
        return extracted_key, new_node

    def add_child(self, child) -> None:
        bisect.insort(self.children, child, key=lambda x: x.get_key(0).get_id())

    def is_leaf(self) -> bool:
        return self.leaf

    def get_keys(self) -> list:
        return self.keys

    def get_key(self, index) -> Student:
        return self.keys[index]

    def has_key(self, index: int) -> bool:
        return index < len(self.keys)

    def has_child(self, index: int) -> bool:
        return index < len(self.children)

    def get_child(self, index: int) -> Student:
        return self.children[index]

    def get_children(self) -> [Student]:
        return self.children

    def get_number_of_children(self) -> int:
        return len(self.children)

    def get_number_of_keys(self) -> int:
        return len(self.keys)

    def has_available_key_space(self) -> bool:
        return len(self.keys) < (2 * self.degree - 1)

    def has_available_child_space(self) -> bool:
        return len(self.children) < (2 * self.degree)

    def __str__(self) -> str:
        return str()
