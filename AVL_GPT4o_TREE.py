# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def is_real_node(self):
        if self.key is None and self.value is None:
            return False
        return True


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.

    """
    NONE_NODE = AVLNode(None, None)

    def __init__(self):
        self.root = AVLTree.NONE_NODE

    """searches for a node in the dictionary corresponding to the key

    @type key: int
    @param key: a key to be searched
    @rtype: AVLNode
    @returns: node corresponding to key
    """

    def search(self, key):
        curr_node = self.root

        while curr_node.is_real_node():
            if curr_node.key == key:
                return curr_node
            elif curr_node.key < key:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

        return None

    """inserts a new node into the dictionary with corresponding key and value

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, key, val):
        parent_node = self.regular_insertion(key, val)
        self.balance_tree(parent_node)

    def balance_tree(self, parent_node):
        while parent_node.is_real_node():
            old_parent_height = parent_node.height
            parent_node.height = 1 + max(
                parent_node.left.height if parent_node.left.is_real_node() else 0,
                parent_node.right.height if parent_node.right.is_real_node() else 0
            )
            parent_bf = (
                    (parent_node.left.height if parent_node.left.is_real_node() else 0) -
                    (parent_node.right.height if parent_node.right.is_real_node() else 0)
            )

            if abs(parent_bf) < 2 and (old_parent_height == parent_node.height):
                break
            elif abs(parent_bf) < 2 and (old_parent_height != parent_node.height):
                parent_node = parent_node.parent
            elif parent_bf == 2:
                son_bf = (
                        (parent_node.left.left.height if parent_node.left.left.is_real_node() else 0) -
                        (parent_node.left.right.height if parent_node.left.right.is_real_node() else 0)
                )
                if son_bf == -1:
                    self.left_rotate(parent_node.left)
                self.right_rotate(parent_node)
                break
            elif parent_bf == -2:
                son_bf = (
                        (parent_node.right.left.height if parent_node.right.left.is_real_node() else 0) -
                        (parent_node.right.right.height if parent_node.right.right.is_real_node() else 0)
                )
                if son_bf == 1:
                    self.right_rotate(parent_node.right)
                self.left_rotate(parent_node)
                break

    def left_rotate(self, criminal):
        node_A = criminal.right
        criminal.right = node_A.left
        if node_A.left.is_real_node():
            node_A.left.parent = criminal
        node_A.left = criminal
        node_A.parent = criminal.parent

        if criminal.parent is AVLTree.NONE_NODE:
            self.root = node_A
        elif criminal.parent.left is criminal:
            criminal.parent.left = node_A
        else:
            criminal.parent.right = node_A

        criminal.parent = node_A

        criminal.height = 1 + max(
            criminal.left.height if criminal.left.is_real_node() else 0,
            criminal.right.height if criminal.right.is_real_node() else 0
        )
        node_A.height = 1 + max(
            node_A.left.height if node_A.left.is_real_node() else 0,
            node_A.right.height if node_A.right.is_real_node() else 0
        )

    def right_rotate(self, criminal):
        node_A = criminal.left
        criminal.left = node_A.right
        if node_A.right.is_real_node():
            node_A.right.parent = criminal
        node_A.right = criminal
        node_A.parent = criminal.parent

        if criminal.parent is AVLTree.NONE_NODE:
            self.root = node_A
        elif criminal.parent.left is criminal:
            criminal.parent.left = node_A
        else:
            criminal.parent.right = node_A

        criminal.parent = node_A

        criminal.height = 1 + max(
            criminal.left.height if criminal.left.is_real_node() else 0,
            criminal.right.height if criminal.right.is_real_node() else 0
        )
        node_A.height = 1 + max(
            node_A.left.height if node_A.left.is_real_node() else 0,
            node_A.right.height if node_A.right.is_real_node() else 0
        )

    def regular_insertion(self, key, val):
        parent = AVLTree.NONE_NODE
        curr_node = self.root
        new_node = AVLNode(key, val)
        new_node.height = 1

        new_node.left = AVLTree.NONE_NODE
        new_node.right = AVLTree.NONE_NODE

        while curr_node.is_real_node():
            parent = curr_node
            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        new_node.parent = parent

        if not parent.is_real_node():
            self.root = new_node
        elif key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        return parent

    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, node):
        return -1

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of touples (key, value) representing the data structure
    """

    def avl_to_array(self):
        return None

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    """

    def size(self):
        return self.root.left.size + self.root.right.size + 1

    """compute the rank of node in the dictionary

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary to compute the rank for
    @rtype: int
    @returns: the rank of node in self
    """

    def rank(self, node):
        return -1

    """finds the i'th smallest item (according to keys) in the dictionary

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: AVLNode
    @returns: the node of rank i in self
    """

    def select(self, i):
        return None

    """finds the node with the largest value in a specified range of keys

    @type a: int
    @param a: the lower end of the range
    @type b: int
    @param b: the upper end of the range
    @pre: a<b
    @rtype: AVLNode
    @returns: the node with maximal (lexicographically) value having a<=key<=b, or None if no such keys exist
    """

    def max_range(self, a, b):
        return None

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    """

    def get_root(self):
        return self.root if self.root.is_real_node() else None


def print_space(n, removed):
    for i in range(n):
        print("\t", end="")
    if removed is None:
        print(" ", end="")
    else:
        print(removed.key, end="")

def print_binary_tree(root):
    tree_level = []
    temp = []
    tree_level.append(root)
    counter = 0
    height = root.height
    number_of_elements = 2 ** (height + 1) - 1
    while counter <= height:
        removed = tree_level.pop(0)
        if len(temp) == 0:
            print_space(int(number_of_elements /
                            (2 ** (counter + 1))), removed)
        else:
            print_space(int(number_of_elements / (2 ** counter)), removed)
        if removed is None:
            temp.append(None)
            temp.append(None)
        else:
            temp.append(removed.left)
            temp.append(removed.right)
        if len(tree_level) == 0:
            print("\n")
            tree_level = temp
            temp = []
            counter += 1
def main():
    myTree = AVLTree()
    myTree.insert(5, '1')
    myTree.insert(2, '1')
    myTree.insert(3, '1')
    myTree.insert(1, '1')
    myTree.insert(0, '1')

    print_binary_tree(myTree.root)

if __name__ == "__main__":
    main()