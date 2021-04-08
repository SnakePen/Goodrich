class ArrayQueue:
    """FIFO queue implementation using a Python list as
    container of data.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
       return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue. 

        Raise exception if the queue is empty. 
        """
        if self.is_empty():
            ('Queue is empty')
            return
        return self._data[self._front]

    def dequeue(self):

        if self.is_empty():
            print('Queue is empty')
            return
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self,element):
        """Add an element to the back of the queue"""
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) # double the array size.
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = element
        self._size += 1

    def _resize(self, cap):

        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

Q = ArrayQueue()
Q.enqueue(3)
Q.enqueue(5)
Q.enqueue(7)
Q.enqueue(11)

while Q.is_empty() is False:
    print(Q.dequeue())
print(Q.first)