from classes import BTreeNode, Student


class BTree:

    def __init__(self, root: BTreeNode = None, order: int = 3):
        self.root: BTreeNode = root
        self.order: int = order

    # https://www.geeksforgeeks.org/insert-operation-in-b-tree/
    def insert(self, value: Student) -> None:
        if self.root is None:
            self.root = BTreeNode(leaf=True, order=self.order)
        insertion_node = self.find_node_by_value(value)
        # If node has space, then all's good, insert the value and move on
        insertion_node.insert_key(value)
        while not insertion_node.has_available_key_space():
            parent_node = self.find_parent_node(insertion_node)
            insertion_node = self.split_child(parent_node, insertion_node)
        return

    def split_child(self, parent_node: BTreeNode, child_node: BTreeNode) -> BTreeNode:
        add_value, new_node = child_node.split_node()
        if not parent_node:
            parent_node = BTreeNode(leaf=False, order=self.order)
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
                result = self.find_parent_node(node, child)
                if result is not None:
                    return result
        return None

    def find_node_by_value(self, value: Student) -> BTreeNode:
        traversed_node: BTreeNode = self.root
        # Node traversal
        while not traversed_node.is_leaf():
            for i in range(traversed_node.get_number_of_keys()):
                if value.get_id() < traversed_node.get_key(i).get_id():
                    traversed_node = traversed_node.get_child(i)
                    break
                elif (i + 1 < traversed_node.get_number_of_keys()
                      and traversed_node.get_key(i).get_id() < value.get_id() < traversed_node.get_key(i + 1).get_id()):
                    traversed_node = traversed_node.get_child(i + 1)
                    break

                elif i + 1 == traversed_node.get_number_of_keys():
                    traversed_node = traversed_node.get_child(-1)
                    break

        return traversed_node

    def find_node_by_id(self, id: int) -> BTreeNode:
        traversed_node: BTreeNode = self.root
        # Node traversal
        while not traversed_node.is_leaf():
            if traversed_node.has_key_with_id(id):
                return traversed_node
            for i in range(traversed_node.get_number_of_keys()):
                if id < traversed_node.get_key(i).get_id():
                    traversed_node = traversed_node.get_child(i)
                    break
                elif (i + 1 < traversed_node.get_number_of_keys()
                      and traversed_node.get_key(i).get_id() < id < traversed_node.get_key(i + 1).get_id()):
                    traversed_node = traversed_node.get_child(i + 1)
                    break

                elif i + 1 == traversed_node.get_number_of_keys():
                    traversed_node = traversed_node.get_child(-1)
                    break

        return traversed_node

    def search(self, id: int, node: BTreeNode = None) -> Student:
        if node is None:
            node = self.root
        i = 0
        while i < node.get_number_of_keys() and id > node.get_key(i).get_id():
            i += 1
        if i < node.get_number_of_keys() and id == node.get_key(i).get_id():
            return node.get_key(i)
        if node.is_leaf():
            return None
        return self.search(id, node.get_child(i))

    # https://www.programiz.com/dsa/deletion-from-a-b-tree
    def delete(self, id: int) -> None:
        delete_node = self.find_node_by_id(id)
        if delete_node is None:
            raise KeyError("Key not found")

        remove_index = delete_node.remove_key(id)
        if delete_node.is_leaf():
            while delete_node and not delete_node.has_aleast_minimum_keys():
                parent_node = self.find_parent_node(node=delete_node)
                delete_node = self.delete_from_leaf(node=delete_node, parent_node=parent_node)
                if delete_node == self.root and self.root.has_no_keys():
                    self.root = delete_node.get_child(0)
                    break
        else:
            while delete_node and not delete_node.has_aleast_minimum_keys():
                parent_node = self.find_parent_node(node=delete_node)
                delete_node = self.delete_from_internal_node(node=delete_node, parent_node=parent_node,
                                                             delete_index=remove_index)

    # Case 1
    def delete_from_leaf(self, node: BTreeNode, parent_node: BTreeNode) -> BTreeNode:
        if parent_node is None:
            return None
        child_index = parent_node.get_child_index(node)
        if child_index > 0 and parent_node.get_child(child_index - 1).has_more_than_minimum_keys():
            return self.borrow_key_from_left_sibling(parent_node=parent_node, node=node)
        if (child_index < parent_node.get_number_of_children() - 1 and
                parent_node.get_child(child_index + 1).has_more_than_minimum_keys()):
            return self.borrow_key_from_right_sibling(parent_node=parent_node, node=node)
        if child_index > 0:
            new_node = self.merge_nodes(left_child=parent_node.get_child(child_index - 1), right_child=node)
            parent_node.remove_child(node)
            parent_node.remove_child(parent_node.get_child(child_index - 1))
            borrowed_key = parent_node.remove_key_by_index(child_index - 1)
            new_node.insert_key(borrowed_key)
            parent_node.add_child(new_node)
            return parent_node
        if child_index < parent_node.get_number_of_children() - 1:
            new_node = self.merge_nodes(left_child=node, right_child=parent_node.get_child(child_index + 1))
            parent_node.remove_child(node)
            parent_node.remove_child(parent_node.get_child(child_index))
            borrowed_key = parent_node.remove_key_by_index(child_index)
            new_node.insert_key(borrowed_key)
            parent_node.add_child(new_node)
            return parent_node

    def delete_from_internal_node(self, node: BTreeNode, parent_node: BTreeNode, delete_index: int) -> BTreeNode:
        if delete_index > 0:
            left_child = node.get_child(delete_index - 1)
            if left_child.has_more_than_minimum_keys():
                borrowed_key = left_child.remove_key_by_index(-1)
                node.insert_key(borrowed_key)
                return parent_node
        if delete_index < parent_node.get_number_of_children():
            right_child = node.get_child(delete_index + 1)
            if right_child.has_more_than_minimum_keys():
                borrowed_key = right_child.remove_key_by_index(0)
                node.insert_key(borrowed_key)
                return parent_node
        if node.get_child(delete_index - 1).has_exactly_minimum_keys() and node.get_child(
                delete_index + 1).has_exactly_minimum_keys():
            new_node = self.merge_nodes(node.get_child(delete_index - 1), node.get_child(delete_index + 1))
            parent_node.remove_child(delete_index - 1)
            parent_node.remove_child(delete_index - 1)
            parent_node.add_child(new_node)
            return parent_node
        return None

    @staticmethod
    def borrow_key_from_left_sibling(parent_node: BTreeNode, node: BTreeNode) -> BTreeNode:
        child_index = parent_node.get_child_index(node)
        left_sibling = parent_node.get_child(child_index - 1)
        borrowed_key = left_sibling.remove_key_by_index(-1)
        borrowed_parent_key = parent_node.remove_key_by_index(child_index - 1)
        parent_node.insert_key(borrowed_key)
        node.insert_key(borrowed_parent_key)
        if not left_sibling.has_no_children():
            transfer_child = left_sibling.remove_child_by_index(-1)
            node.add_child(transfer_child)
        return node

    @staticmethod
    def borrow_key_from_right_sibling(parent_node: BTreeNode, node: BTreeNode) -> BTreeNode:
        child_index = parent_node.get_child_index(node)
        right_sibling = parent_node.get_child(child_index + 1)
        borrowed_key = right_sibling.remove_key_by_index(0)
        borrowed_parent_key = parent_node.remove_key_by_index(child_index)
        parent_node.insert_key(borrowed_key)
        node.insert_key(borrowed_parent_key)
        if not right_sibling.has_no_children():
            transfer_child = right_sibling.remove_child_by_index(0)
            node.add_child(transfer_child)
        return node

    def merge_nodes(self, left_child: BTreeNode, right_child: BTreeNode, leaf: bool = None) -> BTreeNode:
        if leaf is None:
            leaf = left_child.is_leaf()
        new_node = BTreeNode(leaf, order=self.order)
        if (left_child.get_number_of_children() + right_child.get_number_of_children()) > self.order:
            left_node = left_child.remove_child_by_index(-1)
            right_node = right_child.remove_child_by_index(0)
            new_node.add_child(self.merge_nodes(left_node, right_node))
        for child in left_child.get_children() + right_child.get_children():
            new_node.add_child(child)
        for key in left_child.get_keys() + right_child.get_keys():
            new_node.insert_key(key)
        return new_node

    def __repr__(self, node=None, level=0):
        if self.root.has_no_keys():
            return str([])
        if not node:
            node = BTreeNode(leaf=False)
            node.add_child(self.root)
        if node.is_leaf():
            return {level: [node.get_keys()]}
        result = {level: [node.get_keys()]}
        for child in node.get_children():
            searched = self.__repr__(child, level + 1)
            for key, value in searched.items():
                if key in result:
                    result[key].extend(value)
                else:
                    result[key] = value

        if level != 0:
            return result
        else:
            return_str = ''
            for key, value in result.items():
                if key != 0:
                    return_str += f'Level {key}:' + ' ' * (80 - key * 15)
                    for val in value:
                        return_str += f'{val}'
                    return_str += '\n'

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
