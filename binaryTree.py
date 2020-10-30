class Node:
	#Iniatialize Binary Tree
	def __init__(self,data):
		self.left=None
		self.right=None
		self.data=data

	def insert(self,data):
		if self.data:
			if data<self.data:
				#If left node is empty, insert data
				if self.left is None:
					self.left=Node(data)
				else:
					self.left.insert(data)
			elif data>self.data:
				if self.right is None:
					self.right=Node(data)
				else:
					self.right.insert(data)
		else:
			self.data=data

	def PrintTree(self):
		if self.left:
			self.left.PrintTree()
		print self.data,
		if self.right:
			self.right.PrintTree()

	def findval(self, lkpval):
		if lkpval < self.data:
			if self.left is None:
				return str(lkpval)+" is not Found"
			return self.left.findval(lkpval)
		elif lkpval > self.data:
			if self.right is None:
				return str(lkpval)+" is not Found"
			return self.right.findval(lkpval)
		else:
			return str(self.data) + " is found"

	#left -> root -> right
	def inorderTraversal(self, root):
		res = []
		if root:
			res = self.inorderTraversal(root.left)
			res.append(root.data)
			res = res + self.inorderTraversal(root.right)
		return res

	#left-> right-> root
	def postOrderTravesal(self,root):
		res=[]
		if root:
			res=self.postOrderTravesal(root.left)
			# print res
			res=res + self.postOrderTravesal(root.right)
			# print res
			res.append(root.data)
		return res
	def preOrderTraversal(self,root):
		res=[]
		if root:
			res.append(root.data)
			res=res+self.preOrderTraversal(root.left)
			res=res+self.preOrderTraversal(root.right)
		return res

def maxDepth(root):
	if root==None:
		return 0
	leftD=maxDepth(root.left)
	rightD=maxDepth(root.right)

	if leftD>rightD:
		return leftD+1
	else:
		return rightD+1

# 

# def find_max(self):
#         if self.right is None:
#             return self.data
#         return self.right.find_max()

root = Node(12)

#Nodes of BST
node_list=[11,16,18,19,6]
for nl in node_list:
	root.insert(nl)
# root.PrintTree()

print "inorder"
print root.inorderTraversal(root)
print "postorder"
print root.postOrderTravesal(root)
print "preorder"
print root.preOrderTraversal(root)
print "left items"
# print root.find_max(root)

print maxDepth(root)
print "Searching BST"
print root.findval(6)
print root.findval(100)

# print Node.inOrder(root)