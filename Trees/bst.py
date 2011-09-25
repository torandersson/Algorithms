"""
Tor Andersson
site: AllTheIssues.com

Binary search tree with no parent reference makes it a little bit trickier..

Delete 3 cases

1) No children delete it
2) Remove and replace
3) 2 children, find min and swap =)


"""

class BinarySearchTree(object):
	
	def __init__(self):
		self.root = None

	def insert(self,new_node):
		if not self.root:
			self.root = new_node
		else:
			self.insert_node(self.root,new_node)
			
	
	def insert_node(self,current,new_node):
		if new_node.key >= current.key:
			if not current.left:
				current.left = new_node
			else:
				self.insert_node(current.left,new_node)
		else:
			if not current.right:
				current.right = new_node
			else:
				self.insert_node(current.right,new_node)
	
	def delete(self,key):
		self.delete_traverse(self.root,key)
			
	def delete_traverse(self,node,key):
		if node.left and node.left.key == key:
			if not node.left.left and not node.left.right:
				node.left = None
			elif not node.left.left and node.left.right:
				node.left = node.left.right
			elif node.left.left and not node.left.right:
				node.left = node.left.left
			else:
				replace = self.find_min(node.left.left)
				replace.right = node.left.right
				replace.left = node.left.left
				node.left = replace
		
		elif node.right and node.right.key == key:
			if not node.right.left and not node.right.right:
				node.right = None
			elif not node.right.left and node.right.right:
				node.right = node.right.right
			elif node.right.left and not node.right.right:
				node.right = node.right.left
			else:
				replace = selffind_min(node.right.left)
				replace.right = node.right.right
				replace.left = node.right.left
				node.right = replace
		elif key > node.key:
			self.delete_traverse(node.left,key)
		elif key < node.key:
			self.delete_traverse(node.right.key)
						
				
	def find_min(self,node):
		found = None
		if node.right:
			found =  find_min(node.right())
		else:
			return found
		if found.left:
			node.right = found.left
			found.left = None
		return found
		
	def search_by_key(self,key):
		return self.search_traverse(self.root,key)
			
	def search_traverse(self,node,key):
		if node.key == key:
			return node
		elif key >= node.key:
			return self.search_traverse(node.left,key)
		elif key < node.key:
			return self.search_traverse(node.right,key)
			
	def printer(self):
		print
		self.traverse_printer(self.root)
			
	def traverse_printer(self,node):
		if node.left:
			self.traverse_printer(node.left)
		print node.key
		if node.right:
			self.traverse_printer(node.right)
	
class Node:
	def __init__(self):
		self.left = None
		self.right = None
		self.value = None	
		self.key = None
		
