# Implementing stack using lists

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self, data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]


# implementing Queue using lists

class Queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def enqueue(self, data):
		self.items.insert(0, data)

	def dequeue(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]