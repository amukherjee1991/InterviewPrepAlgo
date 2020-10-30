class Node:
	#constructor
	def __init__(self,data,next=None):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None

	def insert(self,data):
		newNode=Node(data)
		if self.head:
			current=self.head
			while current.next:
				current=current.next
			current.next=newNode
		else:
			self.head=newNode

	def printLL(self):
		current=self.head
		print current.data
		while current:
			print current.data
			current=current.next
			# pass

LL=LinkedList()
LL.insert(19)
LL.insert(1)
LL.insert(5)
LL.insert(9)
LL.insert(110)

LL.printLL()