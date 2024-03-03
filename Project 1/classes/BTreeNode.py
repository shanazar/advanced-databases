from classes import Student
import bisect


class BTreeNode:

    def __init__(self, leaf=False, order: int = 3):
        self.leaf = leaf
        self.keys = []
        self.children = []
        self.order = order
        # self.max_keys = depth * 2 - 1
        # self.max_children = depth * 2

    def set_leaf(self, leaf: bool) -> None:
        self.leaf = leaf

    def insert_key(self, key: Student) -> None:
        bisect.insort(self.keys, key, key=lambda x: x.num_id)

    def split_node(self):
        extracted_key = self.keys.pop(self.get_number_of_keys() // 2)
        new_node = BTreeNode(leaf=True, order=self.order)
        for i in range(self.get_number_of_keys() // 2):
            new_node.insert_key(self.keys.pop(0))
        for i in range(self.get_number_of_children() // 2):
            new_node.add_child(self.children.pop(0))
        if new_node.get_number_of_children() > 0:
            new_node.set_leaf(False)
        return extracted_key, new_node

    def add_child(self, child) -> None:
        bisect.insort(self.children, child, key=lambda x: x.get_key(0).get_id())

    def is_leaf(self) -> bool:
        return self.leaf

    def remove_key(self, key: id) -> int:
        i = 0
        for node_key in self.keys:
            i += 1
            if node_key.get_id() == key:
                self.keys.remove(node_key)

        return i

    def remove_child(self, node) -> None:
        self.children.remove(node)

    def set_is_leaf(self, value: bool) -> None:
        self.leaf = value

    def get_keys(self) -> list:
        return self.keys

    def get_key(self, index) -> Student:
        return self.keys[index]

    def has_key(self, index: int) -> bool:
        return index < len(self.keys)

    def get_key_index(self, key: Student) -> int:
        return self.keys.index(key)

    def has_no_keys(self):
        return len(self.keys) == 0

    def has_no_children(self):
        return len(self.children) == 0

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
        return len(self.keys) <= self.order - 1

    def has_exactly_minimum_keys(self):
        return len(self.keys) == self.order // 2

    def has_aleast_minimum_keys(self) -> bool:
        return len(self.keys) >= self.order // 2

    def has_more_than_minimum_keys(self) -> bool:
        return len(self.keys) > self.order // 2

    def remove_key_by_index(self, index: int) -> Student:
        return self.keys.pop(index)

    def remove_child_by_index(self, index: int):
        return self.children.pop(index)

    def get_child_index(self, node) -> int:
        return self.children.index(node)

    def has_available_child_space(self) -> bool:
        return len(self.children) <= self.order

    def has_key_with_id(self, id: int) -> bool:
        for key in self.keys:
            if key.get_id() == id:
                return True
        return False

    def __str__(self) -> str:
        return str(self.keys)

    def __repr__(self) -> str:
        return str(self.keys)
