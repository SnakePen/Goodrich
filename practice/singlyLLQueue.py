class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty')
        return self._head._element

    def dequeue(self):

        if self.is_empty():
            print('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self,e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):
        LinkList = []
        while self.is_empty() is False:
            print(self.dequeue())
            # LinkList.append(self.dequeue())
            if self.__len__() == 0:
                break
        print(self.first())
        LinkList.append(self.first())
        return LinkList


if __name__ == '__main__':
    l1 = LinkedQueue()
    l1.enqueue(10)
    l1.enqueue(20)
    l1.enqueue(30)
    l1.enqueue(40)
    l1.enqueue(50)
    # while l1.is_empty() is False:
    #     print(l1.dequeue())
    #     if l1.__len__() == 0:
    #         break
    #
    # print(l1.first())
    l1.display()