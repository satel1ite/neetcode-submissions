"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        dct = {None: None}
        while curr:
            dct[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            clone = dct[curr]
            clone.next = dct[curr.next]
            clone.random = dct[curr.random]
            curr = curr.next
        return dct[head]