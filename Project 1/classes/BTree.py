from classes import BTreeNode, Student


class BTree:

    def __init__(self, root: BTreeNode = None, degree: int = 3):
        self.root: BTreeNode = root
        self.degree: int = degree

    # https://www.geeksforgeeks.org/insert-operation-in-b-tree/
    def insert(self, value: Student) -> None:
        if self.root is None:
            self.root = BTreeNode(leaf=True, degree=self.degree)

        self.root.insert_key(value)

    def __repr__(self, x=None, level=0):
        if not x:
            x = self.root
        if x.get_number_of_children() == 0:
            return f'{str(x.get_keys())}'
        level_str = f'{x.get_keys()}\n'

        for child in x.get_children():
            level_str += f'{self.__repr__(child, level + 1)}  '
        level_str += '\n'

        return level_str
