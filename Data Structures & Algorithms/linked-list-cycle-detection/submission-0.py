# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast:
            if not fast.next:
                return False
            else:
                fast = fast.next
                if not fast.next:
                    return False
                else:
                    slow = slow.next
                    fast = fast.next
            if slow == fast:
                return True
        return False