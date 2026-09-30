# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        length = 0

        while temp:
            temp = temp.next
            length += 1
        
        odd = False
        if length % 2 == 1:
            length -= 1
            odd = True
        
        length //= 2

        temp = head
        prev = None
        for i in range(length):
            temp = temp.next
        
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt

        temp = prev
        
        for i in range(length - 1):
            headNext = head.next
            tempNext = temp.next
            head.next = temp
            temp.next = headNext
            head = headNext
            temp = tempNext
        
        if odd:
            head.next = temp
        
