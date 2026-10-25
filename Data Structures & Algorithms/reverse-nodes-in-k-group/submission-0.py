# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstHead = None
        temp = head
        prevProbe = None

        while temp:
            probe = temp

            for _ in range(k):
                if probe:
                    probe = probe.next
                else:
                    return firstHead

            groupHead = temp
            prev = probe
            
            for _ in range(k):
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
        
            if prevProbe:
                prevProbe.next = prev
            else:
                firstHead = prev
            
            prevProbe = groupHead


        return firstHead