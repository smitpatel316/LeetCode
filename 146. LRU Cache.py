class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.len = 0
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
            self.len -= 1
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        self.len += 1
        if self.len > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
            self.len -= 1

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    @staticmethod
    def _remove(node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


if __name__ == "__main__":
    c = LRUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    print(c.get(1))
    c.put(3, 3)
    print(c.get(2))
