class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:  # Removing only element
            self._tail = None  # queue becomes empty
        else:
            self._tail._next = oldhead._next  # bypass the old head
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


if __name__ == '__main__':
    l1 = CircularQueue()
    l1.enqueue(10)
    l1.enqueue(20)
    l1.enqueue(30)
    l1.enqueue(40)
    l1.enqueue(50)
    while l1.is_empty() is False:
        print(l1.dequeue())
        if l1.__len__() == 0:
            break
    print(l1.first())
