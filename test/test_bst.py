import unittest2
from Trees.bst import BinarySearchTree, Node
"""
Test for binary search tree
"""
class BstTestClass(unittest2.TestCase):
	
	def setUp(self):
		self.tree = BinarySearchTree()

	def testInsert(self):
		node = Node()
		node.key = 10
		node.value = "tor"
		self.tree.insert(node)
		result = self.tree.search_by_key(10)
		
		self.assertEqual("tor",result.value)
	
		node2 = Node()
		node2.key = 20
		node2.value = "malin"
		self.tree.insert(node2)
		
		result = self.tree.search_by_key(20)
		
		self.assertEqual("malin",result.value)
		
		node3 = Node()
		node3.key = 30
		node3.value = "eira"
		self.tree.insert(node3)
		
		result = self.tree.search_by_key(30)
		
		self.assertEqual("eira",result.value)
		
		node4 = Node()
		node4.key = 25
		node4.value = "truls"
		self.tree.insert(node4)

		result = self.tree.search_by_key(25)

		self.assertEqual("truls",result.value)
		
		node4 = Node()
		node4.key = 6
		node4.value = "glenn"
		self.tree.insert(node4)

		result = self.tree.search_by_key(6)

		self.assertEqual("glenn",result.value)
		
		
		self.tree.printer()
		
	def testDelete(self):
		node = Node()
		node.key = 10
		node.value = "tor"
		self.tree.insert(node)
		
		
		node2 = Node()
		node2.key = 20
		node2.value = "malin"
		self.tree.insert(node2)
		
		node3 = Node()
		node3.key = 30
		node3.value = "eira"
		self.tree.insert(node3)

		node4 = Node()
		node4.key = 25
		node4.value = "truls"
		self.tree.insert(node4)
		
		self.tree.delete(30)	
		self.tree.delete(10)
		
		self.tree.printer()

		
	