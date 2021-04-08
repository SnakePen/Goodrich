class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """create an empty stack"""
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):

        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):

        if self.is_empty():
            print('Stack is empty')
        return self._head._element

    def pop(self):

        if self.is_empty():
            print('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


if __name__ == '__main__':
    list1 = LinkedStack()

    list1.push(5)
    list1.push(7)
    list1.push(9)
    while list1.is_empty() is False:
        print(list1.pop())
    print(list1.top())
