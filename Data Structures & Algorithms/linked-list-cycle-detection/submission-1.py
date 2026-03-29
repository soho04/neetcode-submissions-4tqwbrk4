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
                print(slowpointer.val, fastpointer.val)
                return True
            
            if fastpointer.next:
                fastpointer = fastpointer.next.next
            
            elif not fastpointer.next:
                fastpointer = None
            
            if slowpointer.next:
                slowpointer = slowpointer.next
                print("incremented slowpointer ", slowpointer.val)

        return False

        

        