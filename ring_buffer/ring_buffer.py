# ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted,
# the oldest element in the ring buffer is overwritten with the newest element


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # current acts as the index for storage
        self.current = 0
        self.storage = [None]*capacity

    # adds an element to the list, if full it sets current to first index and places new
    def append(self, item):
        # storage in the current place "index" is where the item should go
        self.storage[self.current] = item

        # if the current value is less than the capacity, add one to current
        # has to be capacity - 1 because you can't go over the capacity
        if self.current < self.capacity - 1:
            self.current += 1
            # print(self.current)

        elif self.current == self.capacity - 1:
            self.current = 0
            # print(self.current)

    # return array of items in placed order
    def get(self):
          # go over each index and return item if index is not None
        return [item for item in self.storage if item is not None]


buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
