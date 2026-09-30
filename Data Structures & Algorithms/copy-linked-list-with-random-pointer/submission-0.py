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
        temp = head
        nodes = dict()
        while temp:
            nodes[temp] = Node(temp.val, None, None)
            temp = temp.next
        
        res = nodes[head]
        copy = None
        while head:
            copy = nodes[head]
            if head.next:
                copy.next = nodes[head.next]
            if head.random:
                copy.random = nodes[head.random]
            head = head.next
        
        return res
