# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visitedHash = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        copy = Node(head.val)
        self.visitedHash[head] = copy
        copy.next = self.copyRandomList(head.next)
        if head.random in self.visitedHash:
            copy.random = self.visitedHash[head.random]
        
        return copy
