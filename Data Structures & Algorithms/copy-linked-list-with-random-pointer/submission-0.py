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
        copyDictionary = {None: None}

        while curr:
            newNode = Node(curr.val)
            copyDictionary[curr] = newNode 
            curr = curr.next

        curr = head

        while curr:
            node = copyDictionary[curr]
            node.next = copyDictionary[curr.next]
            node.random = copyDictionary[curr.random]
            curr = curr.next

        return copyDictionary[head]