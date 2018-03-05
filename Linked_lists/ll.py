class Node:

	def __init__(self, initData):
		self.data = initData
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext



class LinkedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def show(self):
		current = self.head
		while current != None:
			print(current.getData())
			current = current.getNext()

	def remove(self, data):
	  current = self.head
	  previous = None
	  found = False
	  
	  while not found and current.getNext() != None:
	      if current.getData() == data:
	        found = True
	      else:
	        previous = current
	        current = current.getNext()
	        
	  if previous == None:
	    self.head = current.getNext()
	  elif found == True:
	    previous.setNext(current.getNext())
	  elif current.getData() == data:
	    previous.setNext(current.getNext())
	  else:
	    print('Not Found')


	def search(self, data):
		current = self.head
		found = False
		while not found and current.getNext() != None:
			if current.getData() == data:
				found = True
			else:
				current = current.getNext()
		return found


	def append(self, data):
		current = self.head

		while current.getNext() != None:
			current = current.getNext()

		demo = Node(data)
		current.setNext(demo)



mylist = LinkedList()
mylist.add(2)
mylist.add(5)
mylist.add(8)
mylist.remove(1)
mylist.show()
mylist.remove(2)
mylist.show()
mylist.append(2)
mylist.show()