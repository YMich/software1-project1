# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info

"""A class representing a node in an AVL tree"""
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
    @complexity: O(1)
    """
    def is_real_node(self):
        return self is not AVLTree.NONE_NODE


"""
A class implementing an AVL tree.
"""
class AVLTree(object):
    """
    Constructor, you are allowed to add more fields.
    """
    NONE_NODE = AVLNode(float('-inf'), "")
    DELETION = 0
    INSERTION = 1
    PATH_LENGTH_COUNTER = 0

    def __init__(self):
        self.root = AVLTree.NONE_NODE
        self.max_node = AVLTree.NONE_NODE
    # """searches for a node in the dictionary corresponding to the key
    #
    # @type key: int
    # @param key: a key to be searched
    # @rtype: AVLNode
    # @returns: node corresponding to key
    # @complexity: O(log n)
    # """
    # def search(self, key):
    #     curr_node = self.root
    #
    #     while curr_node.is_real_node():
    #         if curr_node.key == key:
    #             return curr_node
    #         elif curr_node.key < key:
    #             curr_node = curr_node.right
    #         else:
    #             curr_node = curr_node.left
    #
    #     return None

    """inserts a new node into the dictionary with corresponding key and value

    @type key: int
    @pre: key currently does not appear in the dictionary
    @param key: key of item that is to be inserted to self
    @type val: string
    @param val: the value of the item
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @complexity: O(log n)
    """
    def insert(self, key, val):
        parent_node = self.regular_insertion(key, val)
        return self.balance_tree(parent_node, AVLTree.INSERTION)

    """
    Balances the AVL tree after insertion or deletion.

    @type parent_node: AVLNode
    @param parent_node: The parent node to start balancing from
    @type mode: int
    @param mode: The balance tree mode, for deleting and insertion the function will work accordingly
    @rtype: int
    @returns: the number of rebalancing operations performed
    @complexity: O(log n)
    """
    def balance_tree(self, parent_node, mode):

        rotation_counter = 0

        while parent_node.is_real_node():
            old_parent_height = parent_node.height
            parent_node.height = 1 + max(parent_node.left.height, parent_node.right.height)
            parent_node.size = 1 + parent_node.left.size + parent_node.right.size
            parent_bf = (parent_node.left.height - parent_node.right.height)

            if abs(parent_bf) < 2 and old_parent_height == parent_node.height:
                break

            elif abs(parent_bf) < 2 and old_parent_height != parent_node.height:
                rotation_counter += 1
                parent_node = parent_node.parent
                continue

            elif abs(parent_bf) == 2:
                if parent_bf == 2:
                    son_bf = parent_node.left.left.height - parent_node.left.right.height

                    if son_bf == -1:
                        self.left_rotate(parent_node.left)
                        rotation_counter += 1
                    self.right_rotate(parent_node)
                    rotation_counter += 1

                elif parent_bf == -2:
                    son_bf = parent_node.right.left.height - parent_node.right.right.height
                    if son_bf == 1:
                        self.right_rotate(parent_node.right)
                        rotation_counter += 1
                    self.left_rotate(parent_node)
                    rotation_counter += 1

                if mode == AVLTree.INSERTION:
                    break

                parent_node = parent_node.parent

        return rotation_counter

    """
    Performs a left rotation on the AVL tree.

    @type criminal: AVLNode
    @param criminal: The node to rotate
    @complexity: O(1)
    """
    def left_rotate(self, criminal):

        node_A = criminal.right
        criminal.right = node_A.left
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

        criminal.height = 1 + max(criminal.left.height, criminal.right.height)
        node_A.height = 1 + max(node_A.left.height, node_A.right.height)

        node_A.size = criminal.size
        criminal.size = criminal.left.size + criminal.right.size + 1

    """
    Performs a right rotation on the AVL tree.

    @type criminal: AVLNode
    @param criminal: The node to rotate
    @complexity: O(1)
    """
    def right_rotate(self, criminal):

        node_A = criminal.left
        criminal.left = node_A.right
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

        criminal.height = 1 + max(criminal.left.height, criminal.right.height)
        node_A.height = 1 + max(node_A.left.height, node_A.right.height)

        node_A.size = criminal.size
        criminal.size = criminal.left.size + criminal.right.size + 1

    """
    Regular insertion method for inserting a node into the AVL tree.

    @type key: int
    @param key: The key of the node to be inserted
    @type val: string
    @param val: The value of the node to be inserted
    @rtype: AVLNode
    @returns: The parent node where the new node was inserted
    @complexity: O(log n)
    """


    def regular_insertion(self, key, val):

        sub_tree_root = self.max_node

        new_node = AVLNode(key, val)
        new_node.height = 0
        new_node.size = 1
        new_node.left = AVLTree.NONE_NODE
        new_node.right = AVLTree.NONE_NODE

        #UP PATH
        while sub_tree_root.is_real_node():
            if sub_tree_root.key > key and sub_tree_root.parent.is_real_node():
                sub_tree_root = sub_tree_root.parent
            else:
                break

        parent = AVLTree.NONE_NODE
        curr_node = sub_tree_root

        #DOWN PATH
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

        if key > self.max_node.key:
            self.max_node = new_node

        return parent






    """deletes node from the dictionary

    @type node: AVLNode
    @pre: node is a real pointer to a node in self
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @complexity: O(log n)
    """
    def delete(self, node):
        parent = self.regular_deletion(node)
        return self.balance_tree(parent, AVLTree.DELETION)

    """
    Regular deletion method for deleting a node from the AVL tree.

    @type node: AVLNode
    @param node: The node to be deleted
    @rtype: AVLNode
    @returns: The parent node of the deleted node
    @complexity: O(log n)
    """
    def regular_deletion(self, node):

        if not node.left.is_real_node() and not node.right.is_real_node():
            self.replace_node(node, AVLTree.NONE_NODE)

        elif node.left.is_real_node() and node.right.is_real_node():
            node_successor = self.get_successor(node)
            self.replace_node_with_successor(node, node_successor)
            return node_successor

        elif node.left.is_real_node():
            self.replace_node(node, node.left)

        elif node.right.is_real_node():
            self.replace_node(node, node.right)

        return node.parent

    """
    Replaces a node in the AVL tree with a new node.

    @type node: AVLNode
    @param node: The node to be replaced
    @type new_node: AVLNode
    @param new_node: The new node to replace with
    @complexity: O(1)
    """
    def replace_node(self, node, new_node):

        if node.parent.is_real_node():
            if node.parent.left is node:
                node.parent.left = new_node
            else:
                node.parent.right = new_node
        else:
            self.root = new_node
        new_node.parent = node.parent

    """
    Replaces a node in the AVL tree with its successor.

    @type node: AVLNode
    @param node: The node to be replaced
    @type successor: AVLNode
    @param successor: The successor node to replace with
    @complexity: O(1)
    """
    def replace_node_with_successor(self, node, successor):

        if successor.parent is not node:
            self.replace_node(successor, successor.right)
            successor.right = node.right
            successor.right.parent = successor
        self.replace_node(node, successor)
        successor.left = node.left
        successor.left.parent = successor

    """
    Finds the successor of a given node in the AVL tree.

    @type node: AVLNode
    @param node: The node to find the successor for
    @rtype: AVLNode
    @returns: The successor node
    @complexity: O(log n)
    """
    def get_successor(self, node):

        if node.right.is_real_node():
            node = node.right
            while node.left.is_real_node():
                node = node.left
            return node
        else:
            while node.parent.left is not node:
                node = node.parent
            return node.parent

    """returns an array representing dictionary 

    @rtype: list
    @returns: a sorted list according to key of tuples (key, value) representing the data structure
    @complexity: O(n)
    """
    def avl_to_array(self):
        arr = []
        def rec_inorder_traversal(root, arr):
            if not root.is_real_node():
                return

            rec_inorder_traversal(root.left, arr)
            arr.append((root.key, root.value))
            rec_inorder_traversal(root.right, arr)

        rec_inorder_traversal(self.root, arr)

        return arr

    """returns the number of items in dictionary 

    @rtype: int
    @returns: the number of items in dictionary 
    @complexity: O(1)
    """
    def size(self):
        return self.root.size

    """compute the rank of node in the dictionary

    @type node: AVLNode
    @pre: node is in self
    @param node: a node in the dictionary to compute the rank for
    @rtype: int
    @returns: the rank of node
    @complexity: O(log n)
    """
    def rank(self, node):
        rank = node.left.size + 1

        while node.parent.is_real_node():
            if node.parent.right is node:
                rank += node.parent.left.size + 1
            node = node.parent

        return rank

    """finds the i'th smallest item (according to keys) in the dictionary

    @type i: int
    @pre: 1 <= i <= self.size()
    @param i: the rank to be selected in self
    @rtype: AVLNode
    @returns: the node of rank i
    @complexity: O(log n)
    """
    def select(self, i):
        curr = self.root

        while curr.is_real_node():
            if curr.left.size + 1 == i:
                return curr
            elif i <= curr.left.size:
                curr = curr.left
            else:
                i -= (curr.left.size + 1)
                curr = curr.right

    """finds the node with the largest value in a specified range of keys

    @type a: int
    @param a: the lower end of the range
    @type b: int
    @param b: the upper end of the range
    @pre: a < b
    @rtype: AVLNode
    @returns: the node with maximal (lexicographically) value having a <= key <= b, or None if no such keys exist
    @complexity: O(log n)
    """
    def max_range(self, a, b):
        return self.rec_max_in_range(self.root, a, b)

    """
    Helper function to find the node with the largest value in a specified range of keys.

    @type node: AVLNode
    @param node: The current node being checked
    @type a: int
    @param a: The lower end of the range
    @type b: int
    @param b: The upper end of the range
    @rtype: AVLNode
    @returns: the node with the maximal value within the range, or NONE_NODE if no such node exists
    @complexity: O(log n)
    """
    def rec_max_in_range(self, node, a, b):

        if not node.is_real_node():
            return AVLTree.NONE_NODE

        if node.key < a:
            return self.rec_max_in_range(node.right, a, b)
        elif node.key > b:
            return self.rec_max_in_range(node.left, a, b)
        else:
            left_max_node = self.rec_max_in_range(node.left, a, b)
            right_max_node = self.rec_max_in_range(node.right, a, b)
            return max(node, left_max_node, right_max_node, key=lambda n: n.value)

    """returns the root of the tree representing the dictionary

    @rtype: AVLNode
    @returns: the root, None if the dictionary is empty
    @complexity: O(1)
    """
    def get_root(self):
        return self.root

    def __repr__(self):
        def printree(root):
            if not root:
                return ["#"]

            root_key = str(root.key)
            left, right = printree(root.left), printree(root.right)

            lwid = len(left[-1])
            rwid = len(right[-1])
            rootwid = len(root_key) + len(str(root.size)) + len(str(root.height)) + 18

            result = [(lwid + 1) * " " + "Key:" + root_key + " Size:"+ str(root.size) + " Height:"+ str(root.height)+ (rwid + 1) * " "]

            ls = len(left[0].rstrip())
            rs = len(right[0]) - len(right[0].lstrip())
            result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

            for i in range(max(len(left), len(right))):
                row = ""
                if i < len(left):
                    row += left[i]
                else:
                    row += lwid * " "

                row += (rootwid + 2) * " "

                if i < len(right):
                    row += right[i]
                else:
                    row += rwid * " "

                result.append(row)

            return result

        return '\n'.join(printree(self.root))

def main():
    myTree = AVLTree()
    myTree.insert(3, 'a')
    myTree.insert(4, 'a')
    myTree.insert(2, 'a')
    myTree.insert(10, 'a')
    myTree.insert(1, 'a')
    myTree.insert(21, 'a')
    myTree.insert(-5, 'a')

    # print_binary_tree(myTree.root)
    # print(myTree.root.key)
    print(myTree)


if __name__ == "__main__":
    main()
