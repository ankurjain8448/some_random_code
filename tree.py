class Node (object) :
	def __init__(self,data):
		self.lchild = None
		self.rchild = None
		self.data = data


class Tree(object):
	
	def InorderSuccessor(self,node):
		parent_node , current_node = self.search(node)
		if current_node.rchild != None:
			temp= current_node.rchild
			while temp.lchild != None :
				temp = temp.lchild
			current_node = temp
		else :
			temp = Tree.root
			pass


	def inorder(self,node):
		if node != None:
			self.inorder(node.lchild)
			print node.data
			self.inorder(node.rchild)

	def search(self,node):
		parent_node = current_node = Tree.root
		while current_node != None:
			if node.data == current_node.data :
				print "node is present"
				break
			elif node.data > current_node.data :
				parent_node = current_node
				current_node = current_node.rchild
			else :
				parent_node = current_node
				current_node = current_node.lchild
		else :
			print "node is not present"
		return parent_node , current_node

	def insert(self,node):
		parent_node , current_node = self.search(node)
		if current_node == None:
			if Tree.root == None :
				Tree.root  = node
			else :
				if node.data < parent_node.data :
					parent_node.lchild = node
				else :
					parent_node.rchild = node


Tree.root = None
t = Tree()
print t
while True:
	n = int(raw_input("enter node ..!!"))
	node = Node(n)
	t.insert(node)
	t.search(node)
	print "__inorder : "
	t.inorder(Tree.root)
