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
            return

        insertion_node = self.find_insertion_node(value)

        # If node has space, then all's good, insert the value and move on
        if insertion_node.has_available_key_space():
            insertion_node.insert_key(value)
            return
        # No space, split the node and find a new target
        add_value, new_node = insertion_node.split_node()
        if insertion_node == self.root:
            self.root = BTreeNode(leaf=False, degree=self.degree)
            self.root.insert_key(add_value)
            self.root.add_child(new_node)
            self.root.add_child(insertion_node)
        else:
            self.root.insert_key(add_value)
            self.root.add_child(new_node)

        if not self.root.has_available_key_space():
            print('Fucking with the root node')
            old_root = self.root
            add_value, new_node = self.root.split_node()
            self.root = BTreeNode(leaf=False, degree=self.degree)
            self.root.insert_key(add_value)
            self.root.add_child(old_root)
            self.root.add_child(new_node)
        self.insert(value)
        return

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
                else:
                    traversed_node = traversed_node.get_child(-1)
                    break

        return traversed_node

    def __repr__(self, x=None):
        if not x:
            x = self.root
        if x.get_number_of_children() == 0:
            return f'{str(x.get_keys())}'

        level_str = f'{x.get_keys()}\n'

        for child in x.get_children():
            level_str += f'{self.__repr__(child)}  '
        level_str += '\n'

        return level_str
