from collections import deque


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.q = deque([])

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.q) == 0:
            self.q.append(self.iterator.next())
        return self.q[0]

    def next(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            return self.q.popleft()
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q) > 0 or self.iterator.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
