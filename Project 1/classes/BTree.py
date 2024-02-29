from classes import BTreeNode, Student


class BTree:

    def __init__(self, root: BTreeNode = None, degree: int = 3):
        self.root: BTreeNode = root
        self.degree: int = degree

    # https://www.geeksforgeeks.org/insert-operation-in-b-tree/
    def insert(self, value: Student) -> None:
        if self.root is None:
            self.root = BTreeNode(leaf=True, degree=self.degree)
        insertion_node = self.find_insertion_node(value)
        # If node has space, then all's good, insert the value and move on
        if insertion_node.has_available_key_space():
            insertion_node.insert_key(value)
            return

        while not insertion_node.has_available_key_space():
            parent_node = self.find_parent_node(insertion_node)
            insertion_node = self.split_child(parent_node, insertion_node)
        return

    def split_child(self, parent_node: BTreeNode, child_node: BTreeNode, value: Student = None) -> BTreeNode:
        add_value, new_node = child_node.split_node(value)
        if not parent_node:
            parent_node = BTreeNode(leaf=False, degree=self.degree)
        parent_node.insert_key(add_value)
        parent_node.add_child(new_node)
        if child_node not in parent_node.get_children():
            parent_node.add_child(child_node)
        if child_node == self.root:
            self.root = parent_node
        return parent_node

    def find_parent_node(self, node: BTreeNode, search_node: BTreeNode = None) -> BTreeNode:
        if search_node is None:
            search_node = self.root
        if node in search_node.get_children():
            return search_node
        for child in search_node.get_children():
            if not child.is_leaf():
                return self.find_parent_node(node, child)
        return None

    def find_insertion_node(self, value: Student) -> BTreeNode:
        traversed_node: BTreeNode = self.root
        # Node traversal
        while not traversed_node.is_leaf():
            for i in range(len(traversed_node.get_keys())):
                if value.get_id() < traversed_node.get_key(i).get_id():
                    traversed_node = traversed_node.get_child(i)
                    break
                elif (i + 1 < len(traversed_node.get_keys())
                      and traversed_node.get_key(i).get_id() < value.get_id() < traversed_node.get_key(i + 1).get_id()):
                    traversed_node = traversed_node.get_child(i + 1)
                    break
                elif i + 1 == len(traversed_node.get_keys()):
                    traversed_node = traversed_node.get_child(-1)
                    break

        return traversed_node

    def __repr__(self, node=None, level=0, index=0, has_neighbors=False):
        if not node:
            node = BTreeNode(leaf=False)
            node.add_child(self.root)
        if node.is_leaf():
            return ''
        if index == 0:
            return_str = ' ' * (50 - level * 17)
        else:
            return_str = ''
        for child in node.get_children():
            return_str += f'{str(child.get_keys())}{" " * level * 3}'
        if not has_neighbors:
            return_str += '\n'
        for i in range(len(node.get_children())):
            child = node.get_child(i)
            return_str += self.__repr__(child, level=level + 1, index=index + i,
                                        has_neighbors=(len(node.get_children()) > 1))

        return return_str

    def get_as_list(self, node=None) -> list:
        returnable = []
        if not node:
            node = self.root
        for i in range(node.get_number_of_children() + node.get_number_of_keys()):
            if node.has_child(i):
                returnable.extend(self.get_as_list(node.get_child(i)))
            if node.has_key(i):
                returnable.append(node.get_key(i).get_id())
        return returnable
