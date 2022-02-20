# Node class
class Node:
	def __init__(self, data):
		self.key = data
		self.right = None
		self.left = None

# **********************************************************************************************************************************************

# Binary Tree class implementation
class Tree:

	def __init__(self):
		self.root = None
		self.found = False
		#only used for deleting nodes in Tree
		self.list = []

	# function to insert element in Tree
	def insert(self, data):
		self.list.append(data)
		# if the root is empty
		if not self.root:
			self.root = Node(data)
			return
		# otherwise we create a queue (FIFO)
		temp = self.root
		nodes = []
		nodes.append(temp)
		# insert element in the first available place
		# level order travesal
		while(len(nodes)):
			temp = nodes[0]
			nodes.pop(0)
			if (not temp.left):
				temp.left = Node(data)
				break
			else:
				nodes.append(temp.left)
			if (not temp.right):
				temp.right = Node(data)
				break
			else:
				nodes.append(temp.right)
	
	# function to search element in Tree
	def search(self, data):
		self.found = False
		self.searchNode(self.root, data)

	def searchNode(self, current, data):
		if(not current):
			return
		if(current.key == data):
			print("\nFound!")
			self.found = True
			return
		if(not self.found):
			self.searchNode(current.left, data)
			self.searchNode(current.right, data)

	# function to delete element in Tree
	def delete(self, data):
		self.found = False
		if data in self.list:
			self.list[self.list.index(data)] = self.list[-1]
			self.deleteNode(self.root, data)
		else:
			print("\nNothing found to delete!")

	def deleteNode(self, current, data):
		if(not current):
			return
		if(current.key == data):
			self.found = True
			current.key = self.list[-1]
			self.FindLastNodeParent()
			return
		if(not self.found):
			self.deleteNode(current.left, data)
			self.deleteNode(current.right, data)
		
	def FindLastNodeParent(self):
		isEven = False
		lastNodeIndex = len(self.list) - 1
		#if it's even (right child)
		if(lastNodeIndex % 2 == 0):
			isEven = True
			ParentIndex = int((lastNodeIndex / 2) - 1)
		#if it's odd (left child)
		else:
			ParentIndex = int(lastNodeIndex / 2)
		ParentData = self.list[ParentIndex]
		self.RemoveLastNode(self.root, ParentData, isEven)
		self.list.pop()
		return

	def RemoveLastNode(self, current, data, isEven):
		self.found = False
		if(not current):
			return
		if(current.key == data):
			self.found = True
			if isEven:
				current.right = None
			else:
				current.left = None
			return
		if(not self.found):
			self.RemoveLastNode(current.left, data, isEven)
			self.RemoveLastNode(current.right, data, isEven)


# ***********************************************************************************************************************************************

# Binary Search Tree class implementation


class BST:

	def __init__(self):
		self.root = None

	# function to insert element in BST
	def insert(self, data):
		data = int(data)
		self.insertNode(self.root, data)

	def insertNode(self, current, data):
		if(current is None):
			self.root = Node(data)
			return
		if(data <= current.key):
			if(current.left):
				self.insertNode(current.left, data)
			else:
				current.left = Node(data)
		elif(data > current.key):
			if(current.right):
				self.insertNode(current.right, data)
			else:
				current.right = Node(data)

	# function to search element in BST
	def search(self, data):
		data = int(data)
		self.searchNode(self.root, data)

	def searchNode(self, current, data):
		if(current.key == data):
			print("\nFound!")
			return
		if(current.key < data):
			if(current.right):
				self.searchNode(current.right, data)
			else:
				print("\nNot found!")
		else:
			if(current.left):
				self.searchNode(current.left, data)
			else:
				print("\nNot found!")

	# function to delete element in BST
	def delete(self, data):
		data = int(data)
		self.deleteNode(self.root, data)

	def deleteNode(self, current, data):
		if current.key == data:
			# 4 possibilities
			# no children
			if not current.left and not current.right:
				return None
			# one right child
			if not current.left and current.right:
				return current.right
			# one left child
			if current.left and not current.right:
				return current.left
			# two children
			pointer = current.right
			while pointer.left:
				pointer = pointer.left
			current.key = pointer.key
			current.right = self.deleteNode(current.right, current.key)

		elif current.key > data:
			if(current.left):
				current.left = self.deleteNode(current.left, data)
			else:
				print("\nNothing found to delete!")
		else:
			if(current.right):
				current.right = self.deleteNode(current.right, data)
			else:
				print("\nNothing found to delete!")

		return current

#inorder travesal
def inorder(node):
		if (not node):
			return
		inorder(node.left)
		print(node.key, end=" ")
		inorder(node.right)


# ***********************************************************************************************************************************************
# main code
while (True):
	TreeOrBstChoice = input(
		"\nHow can I help you? (note: while the program is running, you can type \"end\" to exit!)\n1)create a Tree    2)create a BST\nYour choice is: ")
	
	treeChoice = True
	while (treeChoice):
		if(TreeOrBstChoice == "1"):
			myTree = Tree()
			treeChoice = False
		elif(TreeOrBstChoice == "2"):
			myTree = BST()
			treeChoice = False
		elif(TreeOrBstChoice.lower() == "end"):
			print()
			exit()
		else:
			TreeOrBstChoice = input("invalid input! please try again: ")

	toDoWithTree = True
	while (toDoWithTree):
		print("\nWhat do you want to do with your Tree?")
		myTreeMenu = input(
				"1)insert node    2)delete node    3)search node    4)print the tree (inorder)\nYour choice is: ")
		
		#if we want to exit
		if(myTreeMenu.lower() == "end"):
			print()
			exit()
		
		# if we want to insert
		elif(myTreeMenu == "1"):
			print(
				"\nYou can insert as many as objects you want and in the end insert *")
			while(True):
				data = input("Data: ")
				if(data == "*"):
					break
				elif(data.lower() == "end"):
					print()
					exit()
				else:
					myTree.insert(data)

		# if we want to delete
		elif(myTreeMenu == "2"):
			if(myTree.root):
				print("\nWhich node to delete?")
				data = input("Data: ")
				myTree.delete(data)
			else:
				print("\nYou haven't added a node to the tree yet!")

		# if we want to search
		elif(myTreeMenu == "3"):
			if(myTree.root):
				print("\nWhich node are you looking for?")
				data = input("Data: ")
				myTree.search(data)
				if(TreeOrBstChoice == "1"):
					if(myTree.found == False):
						print("\nNot Found!")
			else:
				print("\nYou haven't added a node to the tree yet!")
	
		#if we want to print
		elif(myTreeMenu == "4"):
				if(myTree.root):
					print("\nHere is your tree: ", end="")
					inorder(myTree.root)
				else:
					print("\nSorry! There is no tree! :(")
				print()
		else:
			myTreeMenu = input("invalid input! please try again: ")


		isDoneWithTree = input( "\nThe task has been processed!\n\nanything else?\n1)Yes    2)No\n\nYour choice is: ")
		if (isDoneWithTree == "1"):
			print(end="")
		elif (isDoneWithTree == "2"):
			toDoWithTree = False
		elif (isDoneWithTree.lower() == "end"):
			exit()
		else:
			isDoneWithTree = input("invalid input! please try again: ")


	isDoneWithProgram = input( "\nOkay! Do you want to recreate?\n1)Yes    2)No\nYour choice is: ")
	if isDoneWithProgram == "1":
		print("\nIt's good to see you again!", end=" ")
	elif (isDoneWithProgram == "2"):
		print("\nBye!\n")
		exit()
	elif (isDoneWithProgram.lower() == "end"):
		print()
		exit()
	else:
		isDoneWithProgram = input("invalid input! please try again: ")