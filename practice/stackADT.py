class ArrayStack:
	""" Stack is LIFO or Last In First Out ADT.
	We will use python list as a data container of the stack.
	"""
	# Initiate an empty Stack.
	def __init__(self):
		self._data = []

	# Size of the Stack
	def __len__(self):
		return len(self._data)

	# Check the stack is empty or not.
	def is_empty(self):
		return len(self._data) == 0

	# Push new data in to the Stack.
	def push(self, ele):
		self._data.append(ele)

	# To get the top of the Stack, which is actally last element of the
	# list.
	def top(self):
		if self.is_empty():
			print('Stack is empty')
			return
		return self._data[-1]

	# To remove the 1st element the Stack, we will remove the last
	# element of the list, which is the 1st element of the stack.
	def pop(self):
		if self.is_empty():
			print('Stack is empty')
			return
		return self._data.pop()


# Bracket matching Algorithm using Stack ADT.
# def is_matched(expr):
# 	"""Matching bracket of an expression using Stack.
# 	"""
# 	left = '({['
# 	right = ']})'
# 	S = ArrayStack()
# 	for element in expr:
# 		if element in left:
# 			S.push(element)
# 		elif element in right:
# 			if S.is_empty():
# 				return False
# 			if right.index(element) != left.index(S.pop()):
# 				return False
# 	return S.is_empty()

# expr1 = '{(x+y)*(a+b)'
# is_matched(expr1)

# stk = ArrayStack()

# stk.push(5)
# stk.push(7)
# stk.push(10)
# stk.push(14)

# while stk.is_empty() is False:
# 	print(stk.pop())
# stk.top()
