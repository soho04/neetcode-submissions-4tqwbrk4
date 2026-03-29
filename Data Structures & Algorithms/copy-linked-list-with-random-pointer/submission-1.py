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
        copyMap = { None : None} 
        while curr:
            clone = Node(curr.val)
            copyMap[curr] = clone
            curr = curr.next

        curr = head

        while curr:
            clone = copyMap[curr]
            clone.next = copyMap[curr.next]
            clone.random = copyMap[curr.random]
            curr = curr.next



        return copyMap[head]