#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



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
	def __init__(self):
		self.root = None

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
		node = self.regularInsertion(key, val)
		self.size += 1

		#TODO:	Inserted node is a leaf
		# 		Inserted node has one child
		#		Inserted node has two children
		# 		NEED TO CHANGE PARENT HEIGHT + SIZE
		#		NEED TO CHANGE NEW NODE HEIGHT + SIZE

		while node is not None:
			balance_factor = node.left.size - node.right.size

			# |BF|<2 and parent's height has not changed
			if abs(balance_factor) < 2 and (node.height == max(node.left.height, node.right.height)+1):
				break;

			elif abs(balance_factor) < 2 and (node.height != max(node.left.height, node.right.height)+1):
				node = node.parent

			elif abs(balance_factor) == 2:
				#TODO: CHECK WICH OF ROTATIONS THEN APPLY
				pass

	def left_rotate(self, criminal):
		node_A = criminal.right
		criminal.right = node_A.left
		criminal.right.parent = criminal
		node_A.left = criminal
		node_A.parent = criminal.parent

		if node_A.parent.left is node_A:
			node_A.parent.left = node_A
		else:
			node_A.parent.right = node_A
			
		criminal.parent = node_A

	def right_rotate(self, criminal):
		node_A = criminal.left
		criminal.left = node_A.right
		criminal.left.parent = criminal
		node_A.right = criminal
		node_A.parent = criminal.parent

		if node_A.parent.left is node_A:
			node_A.parent.left = node_A
		else:
			node_A.parent.right = node_A

		criminal.parent = node_A

	"""
		inserts a new node into the dictionary with corresponding key and value
		
		@type key: int
		@pre: key currently does not appear in the dictionary
		@param key: key of item that is to be inserted to self
		@type val: string
		@param val: the value of the item
		@rtype: int
		@returns: the parent of the inserted node
	"""
	def regularInsertion(self, key, val):
		parent = None
		curr_node = self.root
		new_node = AVLNode(key, val)
		new_node.height = 0
		new_node.size = 1

		while curr_node.is_real_node():
			parent = curr_node
			if curr_node.key < key:
				curr_node = curr_node.right
			else:
				curr_node = curr_node.left

		# Tree was empty
		if parent is None:
			self.root = new_node
		if parent.key < new_node.key:
			parent.right = new_node
		else:
			parent.left = new_node

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

def main():
	node = AVLNode(1, "hello")
	print(node.is_real_node())

if __name__ == "__main__":
	main()