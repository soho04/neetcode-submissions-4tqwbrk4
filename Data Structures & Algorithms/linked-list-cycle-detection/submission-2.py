# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slowpointer, fastpointer = head, head.next

        while fastpointer:

            if slowpointer == fastpointer:
                return True

            if fastpointer.next:
                fastpointer = fastpointer.next.next

            else:
                fastpointer = None

            slowpointer = slowpointer.next

        return False

        

        